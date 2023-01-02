import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """要mach這個格式<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" 
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; 
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
    if re.search(r"<iframe(.)*><\/iframe>" , s):
        """http://youtube.com/embed/xvFZjo5PgG0
           https://youtube.com/embed/xvFZjo5PgG0
           https://www.youtube.com/embed/xvFZjo5PgG0"""
        url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)" , s)
        if url_pattern:
            #.groups() Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern. 
            #The default argument is used for groups that did not participate in the match; it defaults to None.
            split_url = url_pattern.groups()
            return "https://youtu.be/" + split_url[3]


if __name__ == "__main__":
    main()
