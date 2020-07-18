#!/usr/bin/env python3

# Command line tool to convert font grade to YDS

from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser(description="Climbing grade converter - font to YDS and font to Hueco")
    parser.add_argument('grade', help='The grade to convert, either Font (e.g 8a) or YDS (e.g. 13b)')
    parser.add_argument('type', help="The type of climb, either freeclimb or boulder")
    return parser


def convert_freeclimb():
    freeclimb_grades = {}
    with open("./grades/freeclimb_grades.txt") as f:
        for line in f:
            (key, val) = line.split()
            freeclimb_grades[str(key)] = val
    return freeclimb_grades

def convert_boulder():
    boulder_grades = {}
    with open("./grades/boulder_grades.txt") as f:
        for line in f:
            (key, val) = line.split()
            boulder_grades[str(key.lower())] = val.lower()
    return boulder_grades

def font_grade_converter():
    args = create_parser().parse_args()
    
    grade = args.grade.lower()
    type_of_climb = args.type.lower()

    freeclimb_grades = convert_freeclimb()
    boulder_grades = convert_boulder()

    if type_of_climb == 'boulder':
        for v_scale, font in boulder_grades.items():
            if font == grade:
                print(v_scale)
                break
        else:
            print(f"'{grade}' not a valid bouldering grade")
    elif type_of_climb == 'freeclimb':
        for yds, font_freeclimb in freeclimb_grades.items():
            if font_freeclimb == grade:
                print(yds)
                break
        else:
            print(f"'{grade}' not a valid grade")
    else:
        print(f"'{type_of_climb}' not a valid type, type needs to be freeclimb or boulder")

if __name__ == "__main__":
    font_grade_converter()

