import os
os.chdir(r"./mock_html_files")

for i in xrange(1, 5):
    with open("test_mock_html_" + str(i) + ".html", "wb") as f:
        msg = "".join(["<html><p>I am mock html number ",
                       str(i), ", scrape me!<p></html>"
                       ])
        f.write(msg)
