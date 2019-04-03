Dataset for Automatic Cyberbullying Detection in Polish Laguage

Applied in PolEval 2019 Task 6:
http://poleval.pl/tasks/task6

[Problem definition]

Although the problem of humiliating and slandering people through the Internet has existed almost as long as communication via the Internet between people, the appearance of new devices, such as smartphones and tablet computers, which allow using this medium not only at home, work or school but also in motion, has further exacerbated the problem. Especially recent decade, during which Social Networking Services (SNS), such as Facebook and Twitter, rapidly grew in popularity, has brought to light the problem of unethical behaviors in Internet environments, which has been greatly impairing public mental health in adults and, for the most, in younger users and children. It is the problem of cyberbullying (CB), defined as exploitation of open online means of communication, such as Internet forum boards, or SNS to convey harmful and disturbing information about private individuals, often children and students.

To deal with the problem, researchers around the world have started studying the problem of cyberbullying with a goal to automatically detect Internet entries containing harmful information, and report them to SNS service providers for further analysis and deletion. After ten years of research [1], a sufficient knowledge base on this problem has been collected for languages of well-developed countries, such as the US, or Japan. Unfortunately, still close to nothing in this matter has been done for the Polish language. With this dataset, we aim at filling this gap.

Tasks available under this dataset allow users to try their classification methods to determine whether an Internet entry is classifiable as part of cyberbullying narration or not. The entries contain tweets collected from openly available Twitter discussions. Since much of the problem of automatic cyberbullying detection often relies on feature selection and feature engineering [2], the tweets will be provided as such, with minimal preprocessing. The preprocessing, if used, is applied mostly for cases when information about a private person is revealed to the public.

The goal of the tasks is to classify the tweets into cyberbullying/harmful and non-cyberbullying/non-harmful with the highest possible Precision, Recall, balanced F-score and Accuracy. An additional sub-task focuses on differentiating between various types of harmful information, i.e., cyberbullying or hate-speech.


[Examples of tweets]

Template: “contents”,class (1=harmful, 0=non harmful, etc.):
"Ja mam dla ciebie lepszą propozycję : powieś się gdzieś pod lasem UB-ecka gnido .",1
"macie jej numer zdissujcie ją 8)",1
"huju jebany oddawaj server gnoju glubi frajezre kutasie oddawaj bo cie zajebie huju zzglosilem cie i tak nie będziesz miec konta hahahahahahahhahahahaahha",1
"Czerwone Gitary, Historia jednej znajomości... i parawany które istniały zawsze…",0


[Task description]

Task 1: Harmful vs non-harmful

This task is focused on distinguishing between normal/non-harmful tweets (class: 0) and tweets that contain any kind of harmful information (class: 1). This includes cyberbullying, hate speech and related phenomena. 

Evaluation

File for evaluation should contain only tags (results of classification), one per line, aligned in order corresponding to the order of sentences in test data. For evaluation use the attached Perl script in the following manner to calculate the results:

perl evaluate1.pl results.txt > output.txt

The Perl script calculates Precision, Recall, Balanced F-score and Accuracy. In evaluation one should look primarily at the balanced F-score, with Accuracy as a supporting measure. Furthermore, it is good to keep your scores as close as possible to BEP (break-even-point of Precision and Recall).


Task 2: Type of harmfulness

This task is about distinguishing between three classes: 0 (non-harmful), 1 (cyberbullying), 2 (hate-speech). There are various definitions of both cyberbullying and hate-speech, some of them even putting those two phenomena in the same group. The specific conditions on which we based our annotations for both cyberbullying and hate-speech, which have been worked out during ten years of research are summarized in the literature [1], however, the main and definitive condition to distinguish the two is whether the harmful action is addressed towards a private person(s) (cyberbullying), or a public person/entity/large group (hate-speech).

Evaluation

File for evaluation should contain only tags (results of classification), one per line, aligned in the order corresponding to the order of sentences in test data (provided later). For evaluation use the attached Perl script in the following manner to calculate the results:

perl evaluate2.pl results.txt > output.txt

The Perl script calculates Micro-Average F-score (microF) and Macro-Average F-score (macroF). In evaluation one should look primarily at microF to treat all instances equally since the number of instances is different for each class. The additional macroF, treating equally not all instances, but rather all classes, is used to provide additional insight into the results.


[Authors]

Michał Ptaszyński (ptaszynski@ieee.org), Kitami Institute of Technology, Japan

Agata Pieciukiewicz, Polish-Japanese Academy of Information Technology, Poland

Paweł Dybała, Jagiellonian University in Kraków, Poland


[References]

[1] Michal E. Ptaszynski, Fumito Masui. (2018). “Automatic Cyberbullying Detection: Emerging Research and Opportunities”, IGI Global Publishing (November 2018), ISBN: 9781522552499.

[2] Michal Ptaszynski, Juuso Kalevi Kristian Eronen and Fumito Masui. (2017). "Learning Deep on Cyberbullying is Always Better Than Brute Force", IJCAI 2017 3rd Workshop on Linguistic and Cognitive Approaches to Dialogue Agents (LaCATODA 2017), Melbourne, Australia, August 19-25, 2017
