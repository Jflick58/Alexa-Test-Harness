from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.generate(prefix="I am",temperature=0.8, n=5)


text = ["give me ideas",
"how can I improve my mood",
"what should I do",
"any idea what to do",
"help me improve my mood",
"tell me ways to feel better",
"tell me a way to cheer up",
"give me ideas on how to cheer up",
"suggest things I could do to feel better",
"help me feel better",
"I want to feel better",
"tell me how to improve my mood",
"improve my mood",
"give me ideas to improve my mood"]

textgen.train_on_texts(text, num_epochs=1000,  gen_epochs=1000)