import fileinput
import re

fileBrowser = open("./source/flowbite.browser.css", "r+")
fileFlowBite = open("./source/flowbite.min.css", "r+")
fileHTML = open("./source/flowbite.html", "r+")

# with file:
#     lines = [line.rstrip() for line in file]
textBrowser = fileBrowser.read().rstrip()
textFlowBite = fileFlowBite.read().rstrip()
textFileHTML = fileHTML.read().rstrip()

regex = re.compile(r'\.\w+{.+?}')
regexBody = re.compile(r'{.+?}')

classes = regex.findall(textBrowser)

for classContent in classes:
    body = regexBody.findall(classContent)[0]
    escape = re.escape(body)
    regexWithBody = re.compile(r'\.\w+[\-+\:+\\+\_+\/+\w+]+'+escape)
    bodyFlowBite = regexWithBody.findall(textFlowBite)

    if len(bodyFlowBite) > 0:
        foundedClearClass = regexWithBody.findall(textFlowBite)[0]

        if foundedClearClass != body:
            # print(classContent)
            # print(regexWithBody.findall(textFlowBite)[0])

            dirtyClassName = re.search(r'\.(.+?)\{', classContent).group(1)
            clearClassName = re.search(r'\.(.+?)\{', foundedClearClass).group(1)
            textFileHTML= textFileHTML.replace(dirtyClassName, clearClassName)

            print(dirtyClassName)
            print(clearClassName)
            print('========================================')
    else:
        print(classContent)
        print(body)
        print(escape)
        print(bodyFlowBite)
        print('not found')
        print('--------------------------------------')

with   open('./source/ff.html', 'w') as f:
    f.write(textFileHTML)


regexWithBody = re.compile(r'\.\w+[\-+\:+\\+\_+\/+\w+]+')
regexWithBody2 = re.compile(r'\.\w+[\-+\:+\\+\_+\/+\w+]+'+re.escape("{--tw-translate-y:-50%;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}"))
str = '.peer-placeholder-shown\:translate-y-0{--tw-translate-y:0px;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.peer:-moz-placeholder-shown~.peer-placeholder-shown\:-translate-y-1\/2{--tw-translate-y:-50%;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.peer:placeholder-shown~.peer-placeholder-shown\:-translate-y-1\/2{--tw-translate-y:-50%;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.peer:-moz-placeholder-shown~.peer-placeholder-shown\:scale-100{--tw-scale-x:1;--tw-scale-y:1;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.peer:placeholder-shown~.peer-placeholder-shown\:scale-100{--tw-scale-x:1;--tw-scale-y:1;transform:translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))}.peer:focus~.peer-focus\:left-0{left:0}.peer:focus~.peer-focus\:top-2{top:.5rem}.peer:focus~.peer-focus\:top-1{top:.25rem}.peer:focus~.peer-focus\:-translate-y-6{--tw-translate-y:-1.5rem}.peer:focus~.peer-focus\:-translate-y-4,.peer:focus~.peer-focus'
bodyFlowBite = regexWithBody.findall(str)
bodyFlowBite2 = regexWithBody2.findall(str)
print(bodyFlowBite)
print(bodyFlowBite2)
#
#
# print(re.escape('{padding-bottom:4rem}'))
# regexWithBody = re.compile(rf'\.\w+[\-+\:+\\+\w+]+{"{padding-bottom:4rem}"}')
# print(regexWithBody.findall(textFlowBite)[0])


# print(re.search(f'{str_find}'+r'_\d{4}-\d{2}-\d{2}', text))

# for line in fileinput.input(''):
#     if textToSearch in line :
#         print('Match Found')
#     else:
#         print('Match Not Found!!')
#     tempFile.write( line.replace( textToSearch, textToReplace ) )
fileBrowser.close()
fileFlowBite.close()
fileHTML.close()
