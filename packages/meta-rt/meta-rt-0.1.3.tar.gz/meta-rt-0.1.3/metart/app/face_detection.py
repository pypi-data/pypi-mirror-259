import metacv as mc
from ..model_zoo import load_model, run


class FaceDetection(mc.FaceDetection):
    def __init__(self,
                 model_path: str,
                 input_width: int,
                 input_height: int,
                 use_preprocess=True,
                 pad=None,
                 normal=None,
                 mean=None,
                 std=None,
                 swap=None,
                 confidence_thresh=None,
                 nms_thresh=None,
                 class_names=None,
                 device_id=0):
        super().__init__(model_path,
                         input_width,
                         input_height,
                         use_preprocess,
                         pad,
                         normal,
                         mean,
                         std,
                         swap,
                         confidence_thresh,
                         nms_thresh,
                         class_names)
        self.device_id = device_id
        self.model = None
        self.det_output = None
        self.input_names = None
        self.output_names = None
        self.bindings = None
        self.initialize_model()

    def initialize_model(self):
        self.model, self.input_names, self.output_names, self.bindings = load_model(self.model_path, self.device_id)

    def infer(self, image):
        # 由继承类实现模型推理
        outputs = run(image, self.model, self.input_names, self.output_names, self.bindings)
        self.det_output = [out.reshape(list(self.model.get_binding_shape(i + 1))) for i, out in
                           enumerate(outputs)]
        self.det_output = [self.det_output[i] for i in [0, 3, 6, 1, 4, 7, 2, 5, 8]]
