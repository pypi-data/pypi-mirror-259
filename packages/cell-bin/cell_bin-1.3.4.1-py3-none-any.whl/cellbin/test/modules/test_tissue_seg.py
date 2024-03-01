import glob
import os
import numpy as np
import tifffile
from cellbin.modules import StainType
from cellbin.modules.tissue_segmentation import TissueSegmentation
from cellbin.dnn.tseg.yolo.detector import TissueSegmentationYolo


def main(model_type="bcdu"):
    model_path = r"E:\tissuecut\dataset\tissueseg_bcdu_H_20240201_tf.onnx"
    # model_path = r"D:\code\public\tissuecut\model\weight_rna_220909.onnx"
    # model_path = r"D:\code\envs\tissuecut_yolo\tissueseg_yolo_SH_20230131.onnx"
    input_path = r"E:\test\1"
    out_path = r"E:\test\1\n"
    gpu = "0"
    num_threads = 0

    predict = None
    if model_type == "yolo":
        seg = TissueSegmentationYolo()
        seg.f_init_model(model_path)

        predict = seg.f_predict
    else:
        tissue_bcdu = TissueSegmentation(
            model_path=model_path,
            stype=StainType.HE.value,
            gpu=gpu,
            num_threads=int(num_threads))

        predict = tissue_bcdu.run

    file_lst = glob.glob(os.path.join(input_path, "*.tif"))
    for file in file_lst:
        _, name = os.path.split(file)
        img = tifffile.imread(file)
        mask = predict(img)
        mask = np.uint8(np.multiply(mask,255))
        tifffile.imwrite(os.path.join(out_path, name), mask, compression='zlib')

    return


if __name__ == '__main__':
    import sys

    main("bcdu")
    sys.exit()
