"""
Based on "carnevilpart.exe" originally written by daemon1 on the XenTaX forums (https://forum.xentax.com/viewtopic.php?p=160064&sid=67cd5573373bfc5adc2e15c8aa3afbca#p160064)

Their tool was not open source so I rewrote it. 
"""
import struct
import argparse
import os

array1 = [None] * 12
array2 = [3, 2, 1, 0, 7, 6, 5, 4, 11, 10, 9, 8]


def do_partition_split(partition_filepath, output_dir):
    # Keep fd open until all files are written
    with open(partition_filepath, "rb") as partition_file:
        num1 = 3
        while True:
            partition_file.seek(70656 + num1 * 4096, 0)
            num2 = int()

            while True:
                for i in range(12):
                    array1[i] = partition_file.read(1)

                filename = bytes()

                i = 0
                while (i < 12) and array1[array2[i]] != 0:
                    filename = filename + array1[array2[i]]
                    i = i + 1

                filename = str(filename.decode("utf-8"))
                filename = filename.split("\x00", 1)[0]

                print(filename)

                try:
                    num2 = struct.unpack("i", partition_file.read(4))[0]
                except struct.error:
                    return

                if (not filename) and (num2 == 0):
                    return

                if filename == "":
                    break

                partition_file.read(4)
                num3 = struct.unpack("i", partition_file.read(4))[0]

                pos = partition_file.tell()
                array3 = partition_file.read(num2 * 4)
                partition_file.seek(70656 + num3 * 4096, 0)

                if not os.path.isdir(output_dir):
                    os.mkdir(output_dir)
                filename = os.path.join(output_dir, filename)

                output_file = open(filename, "wb")
                output_file.write(bytes(array3))
                output_file.close()

                partition_file.seek(pos, 0)
            num1 = num2


def parse_args():
    parser = argparse.ArgumentParser()

    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "partition_file", help="Partition file from raw hard drive image"
    )
    optional_args = parser.add_argument_group("optional_arguments")
    optional_args.add_argument(
        "-o",
        "--output_dir",
        default="_extracted_partition",
        required=False,
        help="Direcory to dump files. Will be created if it doesn't exist",
    )

    return parser.parse_args()


if __name__ == "__main__":
    ARGS = parse_args()
    do_partition_split(ARGS.partition_file, ARGS.output_dir)
