import numpy as np

import tensorrt as trt
import pycuda.driver as cuda
import pycuda.autoinit


def load_model(model_path, device_id=0):
    input_names, output_names, bindings = [], [], []

    ctx = cuda.Device(device_id).make_context()
    logger = trt.Logger(trt.Logger.WARNING)
    trt.init_libnvinfer_plugins(logger, '')
    with trt.Runtime(logger) as runtime, open(model_path, "rb") as f:
        engine = runtime.deserialize_cuda_engine(f.read())

    with engine.create_execution_context() as context:
        for e in engine:
            size = trt.volume(engine.get_binding_shape(e))
            dtype = trt.nptype(engine.get_binding_dtype(e))
            host_mem = cuda.pagelocked_empty(size, dtype)
            device_mem = cuda.mem_alloc(host_mem.nbytes)
            bindings.append(int(device_mem))
            if engine.binding_is_input(e):
                input_names.append({'host': host_mem, 'device': device_mem})
            else:
                output_names.append({'host': host_mem, 'device': device_mem})

    return engine, input_names, output_names, bindings, ctx


def run(images, model, input_names, output_names, bindings, ctx):
    input_tensor = np.array(images) if isinstance(images, list) else images[np.newaxis, :, :, :]

    ctx.push()
    with model.create_execution_context() as context:
        stream = cuda.Stream()
        input_names[0]['host'] = np.ravel(input_tensor)
        for _input in input_names:
            cuda.memcpy_htod_async(_input['device'], _input['host'], stream)

        context.execute_async_v2(bindings=bindings, stream_handle=stream.handle)

        for _output in output_names:
            cuda.memcpy_dtoh_async(_output['host'], _output['device'], stream)

        stream.synchronize()
        outputs = [out['host'] for out in output_names]
    ctx.pop()

    return outputs
