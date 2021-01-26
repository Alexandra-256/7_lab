#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 1. Написать программу, которая считывает из текстового файла три предложения и выводит их
# в обратном порядке

if __name__ == '__main__':
    with open('test_text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")

    # Разбить текст на предложения.
    sentences = text.split(". ")

    reverse_sentence = '. '.join(reversed(sentences))
    print(reverse_sentence)