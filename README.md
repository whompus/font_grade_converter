## Climbing grade conversion script

This tool converts climbing grades from Font (French) to YDS (American). It also converts bouldering grades fron Font to Hueco (V-Scale). As of right now, the script is very rudimentary and was more of a fun little project. 

Usage:
1. Make script executable by: `chmod u+x font_converter.py`
2. Run it! For example: `./font_converter.py 8a boulder`

More improvements coming, using this repo to track my progress on more features.

### TODO:

- [ ] - Make grades convert the other way (from YDS to Font and from Hueco to Font)
- [ ] - Make into a proper wheel distribution for ease of use
- [ ] - Figure out how to package the text files so that the script can be run from anywhere, not just the dir that the project resides. This could be solved by the above?