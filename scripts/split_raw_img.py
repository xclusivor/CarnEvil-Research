"""
Based on "carnevilraw.exe" originally written by daemon1 on the XenTaX forums (https://forum.xentax.com/viewtopic.php?p=160064&sid=67cd5573373bfc5adc2e15c8aa3afbca#p160064)

Their tool was not open source so I rewrote it. 
"""
import struct
import argparse
import os


def do_image_split(raw_image_filepath, output_dir):
    with open(raw_image_filepath, "rb") as raw_image:
        raw_image.read(4)  # Read past "TRAP"

        # Get number of partitions
        num_parts = struct.unpack("i", raw_image.read(4))[0]
        print("Number of partitions:", num_parts)
        print("Exracting...\n")

        raw_image.read(8)

        array1 = [None] * num_parts
        array2 = [None] * num_parts

        for i in range(num_parts):
            raw_image.read(4)
            array1[i] = struct.unpack("i", raw_image.read(4))[0]
            array2[i] = struct.unpack("i", raw_image.read(4))[0]

        for i in range(num_parts):
            num2 = array2[i] * 512

            raw_image.seek(array1[i] * 512, 0)

            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)
            filename = os.path.join(output_dir, "part" + str(i))

            print('\t' + filename)

            array3 = raw_image.read(num2)
            partition_file = open(filename, "wb")
            partition_file.write(bytes(array3))
        
        print("Done!")


def parse_args():
    parser = argparse.ArgumentParser()

    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "raw_image", help="Raw hard drive image converted from CHD"
    )
    optional_args = parser.add_argument_group("optional_arguments")
    optional_args.add_argument(
        "-o",
        "--output_dir",
        default="_extracted_raw",
        required=False,
        help="Direcory to dump files. Will be created if it doesn't exist",
    )

    return parser.parse_args()


if __name__ == "__main__":
    ARGS = parse_args()
    do_image_split(ARGS.raw_image, ARGS.output_dir)
