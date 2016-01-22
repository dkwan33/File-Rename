#!python3
import re, glob, os

def main():
    print(os.path.basename(__file__), "running...")

    renamer("*.jpg-large", r"^(.*)\.jpg-large$", r"\1.jpg")
    renamer("*.unsafe", r"^(.*)\.unsafe$", r"\1")
    # renamer("*.doc", r"^(.*)\.doc$", r"new(\1).doc") #forward
    # renamer("*.doc", r"^new\((.*)\)\.doc", r"\1.doc") #reverse
    print(os.path.basename(__file__), "complete...")

def renamer(files, pattern, replacement):
    isRemove = True

    for pathname in glob.glob(files):
        basename = os.path.basename(pathname)
        new_filename = re.sub(pattern, replacement, basename)
        if new_filename != basename:
            try:
                os.rename(pathname, os.path.join(os.path.dirname(pathname), new_filename))
                print ("success: {} changed to -> {}".format(pathname, new_filename))
            except:
                print ("error: {} already exists".format(new_filename))

                if ('isRemove'):
                    try:
                        os.remove(pathname)
                        print ("removed: {} because its a dupe".format(pathname))
                    except:
                        print ("error: cannot remove {}".format(pathname))

if __name__ == "__main__":
    main()
