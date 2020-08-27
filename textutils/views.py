from django.http import HttpResponse
from django.shortcuts import render
import string


def navigator(request):
    return render(request, 'navigator.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def remove_punc_func(text):
    punctuations = string.punctuation
    analyzed_txt = ''
    for char in text:
        if char not in punctuations:
            analyzed_txt = analyzed_txt + char
    return analyzed_txt


def full_caps_func(text):
    analyzed_txt = text.upper()
    return analyzed_txt


def new_line_remover_func(text):
    analyzed_txt = ""
    for char in text:
        if char != '\n' and char != '\r':
            analyzed_txt = analyzed_txt + char
    return analyzed_txt


def extra_space_remover_func(text):
    analyzed_txt = ""
    for index, char in enumerate(text):
        if not(text[index] == " " and text[index + 1] == " "):
            analyzed_txt = analyzed_txt + char
    return analyzed_txt


def char_count_func(text):
    count = 0
    for char in text:
        if char != " ":
            count = count + 1
    return count


def word_count_func(text):
    return len(text.split())


def txt_analyzer(request):

    toAnalyze = request.POST.get('text', 'default')

    isRemovePunc = request.POST.get('removepunc', 'off')
    isFullCaps = request.POST.get('fullcaps', 'off')
    isNewLineRemover = request.POST.get('newlineremover', 'off')
    isExtraSpaceRemover = request.POST.get('extraspaceremover', 'off')
    isCharCount = request.POST.get('charcount', 'off')

    analyzed_txt = ""

    if(toAnalyze == ""):
        return render(request, 'error.html', {'error_msg': "Please enter some text to process"})
    elif(isRemovePunc != "on" and isFullCaps != "on" and isNewLineRemover != "on" and isExtraSpaceRemover != "on" and isCharCount != "on"):
        return render(request, 'error.html', {'error_msg': "Please select a processing tool to process the text"})
    else:
        if(isRemovePunc == 'on'):
            analyzed_txt = remove_punc_func(toAnalyze)
            toAnalyze = analyzed_txt

        if(isFullCaps == "on"):
            analyzed_txt = full_caps_func(toAnalyze)
            toAnalyze = analyzed_txt

        if(isNewLineRemover == 'on'):
            analyzed_txt = new_line_remover_func(toAnalyze)
            toAnalyze = analyzed_txt

        if(isExtraSpaceRemover == 'on'):
            analyzed_txt = extra_space_remover_func(toAnalyze)

        charCount = char_count_func(analyzed_txt)
        wordCount = word_count_func(analyzed_txt)
        charCountPrint = str(charCount) + " Characters | " + \
            str(wordCount) + " Words"

    return render(request, 'analyzer.html', {'analyzed_text': analyzed_txt, 'extra': charCountPrint})
