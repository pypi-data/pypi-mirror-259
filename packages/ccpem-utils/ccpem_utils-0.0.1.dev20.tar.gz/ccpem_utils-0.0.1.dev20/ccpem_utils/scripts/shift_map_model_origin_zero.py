#
#     Copyright (C) 2019 CCP-EM
#
#     This code is distributed under the terms and conditions of the
#     CCP-EM Program Suite Licence Agreement as a CCP-EM Application.
#     A copy of the CCP-EM licence can be obtained by writing to the
#     CCP-EM Secretary, RAL Laboratory, Harwell, OX11 0FA, UK.

import argparse
from ccpem_utils.model import gemmi_model_utils
from ccpem_utils.map.mrcfile_utils import get_mapobjhandle, write_newmapobj
import os


def parse_args():
    parser = argparse.ArgumentParser(description="CCP-EM model tools")
    parser.add_argument(
        "-m",
        "--map",
        required=True,
        help="Input map (MRC)",
    )
    parser.add_argument(
        "-p",
        "--model",
        required=False,
        help="Input atomic model file (PDB or mmCIF/PDBx)",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    # Find map origin
    wrapped_mapobj = get_mapobjhandle(args.map)
    wrapped_mapobj.fix_origin()  # if non-zero nstart and zero origin
    ox, oy, oz = wrapped_mapobj.origin
    wrapped_mapobj.origin = (0.0, 0.0, 0.0)
    wrapped_mapobj.nstart = (0, 0, 0)
    shifted_map = os.path.splitext(os.path.basename(args.map))[0] + "_shifted.mrc"
    write_newmapobj(wrapped_mapobj, shifted_map)
    shifted_model = (
        os.path.splitext(os.path.basename(args.model))[0]
        + "_shifted"
        + os.path.splitext(args.model)[1]
    )
    gemmiutils = gemmi_model_utils.GemmiModelUtils(args.model)
    gemmiutils.shift_coordinates(
        trans_vector=(-ox, -oy, -oz),
        out_model_path=shifted_model,
        remove_charges=False,
    )


if __name__ == "__main__":
    main()
