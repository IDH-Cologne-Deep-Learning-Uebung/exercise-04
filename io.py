file = open("wiki.txt")

content = file.readlines()

file.close()

# print(content)

shortSentences = [s for s in content if len(s) <= 30]
articleSentences = [s for s in content if s.lower().startswith(("der", "die", "das"))]
aprilSentences = [s for s in content if "April" in s]

# for sentence in content:
#     # print(sentence)
#     if len(sentence) <= 30:
#         shortSentences.append(sentence)
#     if sentence.lower().startswith(("der", "die", "das")):
#         articleSentences.append(sentence)
#     if "April" in sentence:
#         aprilSentences.append(sentence)

shortFile = open("short.txt", "w+")
shortFile.writelines(shortSentences)
articleFile = open("articles.txt", "w+")
articleFile.writelines(articleSentences)
aprilFile = open("april.txt", "w+")
aprilFile.writelines(aprilSentences)

# print("short sentences:")
# print(shortSentences)
# print("article sentences:")
# print(articleSentences)
# print("april sentences:")
# print(aprilSentences)

