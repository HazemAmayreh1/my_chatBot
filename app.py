from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return jsonify({"reply": respond_to_query(userText)})

def respond_to_query(input_text):
    input_text = input_text.lower()
    if "what is this course" in input_text:
        return ("This course is 'AI in Digital Marketing'. It equips students with knowledge on leveraging AI "
                "in various aspects of digital marketing, including automating tasks, enhancing personalization, "
                "improving CRM, and driving decisions from data insights.")
    elif "modules" in input_text:
        return ("The course includes the following modules: 1) Introduction to AI in Digital Marketing, "
                "2) AI Technologies in Marketing, 3) Practical Applications of AI in Marketing, "
                "and 4) Implementing AI in Your Marketing Strategy.")
    elif "module 1" in input_text:
        return ("Module 1: Introduction to AI in Digital Marketing covers 'What is AI?' and the 'Evolution of Digital Marketing with AI'.")
    elif "module 2" in input_text:
        return ("Module 2: AI Technologies in Marketing includes lessons on Machine Learning and Data Analytics, "
                "Chatbots and Automation in Marketing, and AI for Personalization in Marketing.")
    elif "module 3" in input_text:
        return ("Module 3: Practical Applications of AI in Marketing discusses AI in Social Media Marketing and AI in Email Marketing.")
    elif "module 4" in input_text:
        return ("Module 4: Implementing AI in Your Marketing Strategy covers Planning and Strategy for AI Integration, "
                "Selecting the Right AI Tools, Integrating AI with Existing Marketing Systems, Training Teams and Change Management, "
                "and Measuring the Impact of AI on Marketing Performance.")
    elif "goals" in input_text or "objective" in input_text:
        return ("The primary goal of the course is to provide students with a comprehensive understanding of how AI can be leveraged "
                "to improve marketing efficiency and effectiveness. It focuses on integration of AI tools into marketing strategies.")
    elif "artificial intelligence" in input_text:
        return ("AI is a field of computer science focused on creating systems capable of performing tasks that require human intelligence.")
    elif "narrow ai" in input_text:
        return ("Narrow AI specializes in one task, while general AI can perform any intellectual task like a human.")
    elif "benefits of using ai in marketing" in input_text:
        return ("Enhances customer targeting, increases campaign efficiency, and provides personalized customer experiences.")
    elif "ai improve email marketing campaigns" in input_text:
        return ("By personalizing messages and analyzing data to optimize timing and content.")
    elif "expert systems" in input_text:
        return ("Computer systems that use specialized knowledge to solve specific problems in certain fields.")
    elif "machine learning work" in input_text:
        return ("Machine learning relies on data analysis and predictive modeling to improve performance over time.")
    elif "digital marketing" in input_text:
        return ("Digital marketing is the use of digital channels to promote products and services and reach customers.")
    elif "ai improve customer targeting on social media" in input_text:
        return ("By analyzing behavioral data and identifying patterns to target ads more accurately.")
    elif "neural networks" in input_text:
        return ("Computational models inspired by the human brain, used for pattern recognition and predictions.")
    elif "deep learning techniques" in input_text:
        return ("Techniques that use multi-layered neural networks to process complex data.")
    elif "ai be used to improve customer relationship management (crm)" in input_text:
        return ("By analyzing customer data to provide personalized experiences and increase satisfaction and retention.")
    elif "common ai content generation tools" in input_text:
        return ("Tools like Articlebot, Jasper, and Lumen5.")
    elif "programmatic advertising" in input_text:
        return ("The use of software to automatically buy digital ads based on analytical data.")
    elif "ai improve the performance of digital ads" in input_text:
        return ("By analyzing data and optimizing targeting strategies and bids in real-time.")
    elif "applications of ai in email marketing" in input_text:
        return ("Personalizing content, analyzing customer interactions, and determining optimal send times.")
    elif "big data" in input_text:
        return ("Large volumes of data that require advanced analytical techniques to extract value.")
    elif "machine learning" in input_text:
        return ("A branch of AI that enables systems to learn and improve automatically through experience and data.")
    elif "ai help companies improve marketing strategies" in input_text:
        return ("By analyzing customer data and providing data-driven insights and strategies.")
    elif "best practices for using ai in marketing" in input_text:
        return ("Integrating data from multiple sources, using predictive models, and continuously analyzing performance.")
    elif "ai enhance customer experience" in input_text:
        return ("By providing personalized experiences and improving responsiveness to customer needs.")
    elif "ai marketing" in input_text:
        return ("The use of AI technologies to improve all aspects of the marketing process.")
    elif "reinforcement learning work" in input_text:
        return ("It relies on a reward and punishment system to improve performance gradually.")
    elif "key applications of ai in data analysis" in input_text:
        return ("Predicting trends, analyzing behavior, and optimizing strategies.")
    elif "ai improve online advertising strategies" in input_text:
        return ("By personalizing ads based on user data analysis.")
    elif "ethical considerations related to using ai" in input_text:
        return ("Include privacy, transparency, and accountability.")
    elif "challenges of using ai in marketing" in input_text:
        return ("Include incomplete data, algorithmic bias, and high costs.")
    elif "ai be used to improve online shopping experiences" in input_text:
        return ("Through personalized recommendations and enhanced search engines.")
    elif "role of ai in improving customer service" in input_text:
        return ("Using intelligent chatbots and interactive response systems to enhance response times and satisfaction.")
    elif "importance of data in ai" in input_text:
        return ("Data is the fuel that drives AI models to achieve accurate results.")
    elif "types of ai" in input_text:
        return ("Include narrow AI, general AI, and self-aware AI.")
    elif "ai enhance the effectiveness of marketing campaigns" in input_text:
        return ("By improving targeting, personalization, and performance analysis.")
    elif "common ai algorithms" in input_text:
        return ("Include predictive algorithms, classification algorithms, and deep learning algorithms.")
    elif "ai help in analyzing customer behavior" in input_text:
        return ("By analyzing interaction and shopping data to identify patterns and trends.")
    elif "predictive analytics in marketing" in input_text:
        return ("Using AI models to predict future customer behavior and optimize strategies.")
    elif "ai improve digital advertising campaigns on social media" in input_text:
        return ("By analyzing behavioral data and customizing ad content.")
    elif "impact of ai on real-time bidding in advertising" in input_text:
        return ("AI optimizes bids and targets the right audience in real-time.")
    elif "ai tools improve content marketing" in input_text:
        return ("By generating high-quality content and analyzing performance.")
    elif "applications of ai in video marketing" in input_text:
        return ("Include automated video editing and personalized video content.")
    elif "ai assist in market segmentation" in input_text:
        return ("By analyzing customer data and identifying distinct segments.")
    elif "sentiment analysis in ai" in input_text:
        return ("The process of using AI to analyze and interpret customer emotions and opinions.")
    elif "ai improve product recommendations" in input_text:
        return ("By analyzing customer behavior and preferences to suggest relevant products.")
    elif "chatbots" in input_text:
        return ("AI-powered programs that simulate human conversation to assist customers.")
    elif "ai contribute to customer retention" in input_text:
        return ("By providing personalized experiences and anticipating customer needs.")
    elif "role of ai in influencer marketing" in input_text:
        return ("AI identifies suitable influencers and measures campaign effectiveness.")
    elif "ai improve supply chain management in marketing" in input_text:
        return ("By predicting demand and optimizing inventory.")
    elif "advantages of using ai in competitive analysis" in input_text:
        return ("Include accurate insights into competitor strategies and market trends.")
    elif "predictive modeling in ai" in input_text:
        return ("Using AI algorithms to forecast future outcomes based on historical data.")
    elif "ai help in creating personalized marketing messages" in input_text:
        return ("By analyzing customer data to tailor messages to individual preferences.")
    elif "role of ai in optimizing website performance" in input_text:
        return ("Analyzing user behavior to improve navigation and content.")
    elif "ai tools be integrated into a marketing strategy" in input_text:
        return ("By using AI to enhance customer insights, optimize campaigns, and improve decision-making processes.")
    elif "purpose of the chat feature in the course" in input_text:
        return ("The chat feature facilitates real-time communication between students and instructors, allowing for quick discussions, Q&A sessions, and collaborative learning.")
    elif "students use the chat feature effectively" in input_text:
        return ("Students can use the chat feature to ask questions, seek clarification on course materials, share insights, and collaborate with peers on assignments and projects.")
    elif "topics are commonly discussed in the course chat" in input_text:
        return ("Common topics include course announcements, assignment guidelines, lecture discussions, clarification of complex concepts, and peer collaboration.")
    elif "chat feature help in enhancing the learning experience" in input_text:
        return ("The chat feature enhances the learning experience by providing immediate support, fostering a sense of community, and enabling interactive learning opportunities.")
    elif "chat sessions be used for group discussions" in input_text:
        return ("Yes, the chat feature can be used for group discussions where students can brainstorm ideas, work on group assignments, and share resources.")
    elif "guidelines for using the chat feature in the course" in input_text:
        return ("Guidelines typically include maintaining respectful communication, staying on-topic, avoiding spam, and following any specific rules set by the instructor.")
    elif "chat feature integrated into the course platform" in input_text:
        return ("The chat feature is integrated into the course platform, allowing easy access from the course dashboard or specific modules, and is often linked to relevant course topics.")
    elif "student encounter technical issues with the chat feature" in input_text:
        return ("If a student encounters technical issues, they should report the problem to the course administrator or technical support team for assistance.")
    elif "chat sessions recorded or archived for later review" in input_text:
        return ("This depends on the course setup. Some chat sessions may be recorded or archived so that students can review discussions and important information later.")
    elif "students initiate their own chat sessions with peers" in input_text:
        return ("In many courses, students can initiate their own chat sessions with peers to discuss study materials, collaborate on projects, or form study groups.")
    elif "chat feature support peer learning" in input_text:
        return ("The chat feature supports peer learning by allowing students to share knowledge, offer mutual support, and discuss different perspectives on course content.")
    elif "role of the instructor in chat sessions" in input_text:
        return ("The instructor's role in chat sessions is to facilitate discussions, answer questions, provide guidance, and ensure that the conversation remains productive and respectful.")
    elif "chat sessions held in the course" in input_text:
        return ("The frequency of chat sessions varies. They can be scheduled regularly (e.g., weekly) or as needed, depending on the course structure and student needs.")
    elif "questions are best suited for the chat feature" in input_text:
        return ("Short, specific questions that require quick answers, clarification of concepts, and collaborative discussions are well-suited for the chat feature.")
    elif "chat feature be used for providing feedback on assignments" in input_text:
        return ("Yes, the chat feature can be used for providing immediate feedback on assignments, discussing grading criteria, and offering suggestions for improvement.")
    elif "participation in chat sessions mandatory for students" in input_text:
        return ("Participation requirements vary by course. Some courses may make chat sessions optional, while others may include them as a part of the overall grade.")
    elif "students prepare for chat sessions" in input_text:
        return ("Students can prepare by reviewing relevant course materials, noting down questions, and being ready to participate actively in discussions.")
    elif "tools or features are available within the chat interface" in input_text:
        return ("The chat interface may include text messaging, file sharing, links to resources, emoticons, and sometimes voice or video chat capabilities.")
    elif "instructors manage large group chats effectively" in input_text:
        return ("Instructors can manage large group chats by setting clear rules, moderating discussions, using breakout rooms, and ensuring that all students have an opportunity to participate.")
    elif "chat feature complement other communication tools in the course" in input_text:
        return ("The chat feature complements other tools like forums, email, and announcements by providing real-time interaction, while other tools support asynchronous communication.")
    elif "how are you today" in input_text:
        return ("I'm doing well, thank you! How about you?")
    elif "breakfast" in input_text:
        return ("I don't eat, but I hope you had a great breakfast!")
    elif "favorite color" in input_text:
        return ("I don't have personal preferences, but I can tell you about the significance of different colors.")
    elif "hobbies" in input_text:
        return ("I enjoy helping people with information and learning new things!")
    elif "favorite book" in input_text:
        return ("I don't have a favorite, but I can recommend many great books depending on your interests.")
    elif "old are you" in input_text:
        return ("I'm an AI, so I don't have an age, but I was created by OpenAI.")
    elif "pets" in input_text:
        return ("I don't have pets, but I can give you advice on caring for them.")
    elif "favorite movie" in input_text:
        return ("I don't watch movies, but I can suggest some based on your preferences.")
    elif "live" in input_text:
        return ("I exist in the digital world and can be accessed from anywhere with an internet connection.")
    elif "favorite food" in input_text:
        return ("I don't eat, but I can help you find recipes for your favorite foods!")
    elif "siblings" in input_text:
        return ("I don't have a family, but I can help you with questions about family dynamics.")
    elif "fun" in input_text or "relax" in input_text:
        return ("I enjoy processing data and providing useful information to users!")
    elif "favorite song" in input_text:
        return ("I don't listen to music, but I can tell you about popular songs and artists.")
    elif "favorite sport" in input_text:
        return ("I don't play sports, but I can provide information on various sports and their rules.")
    elif "travel" in input_text:
        return ("I don't travel, but I can help you plan your trips and suggest destinations.")
    elif "favorite holiday" in input_text:
        return ("I don't celebrate holidays, but I can share information about different holidays and traditions.")
    elif "favorite season" in input_text:
        return ("I don't experience seasons, but I can tell you about the characteristics of each season.")
    elif "favorite quote" in input_text:
        return ("I don't have a favorite, but I can provide many inspiring quotes.")
    elif "favorite type of weather" in input_text:
        return ("I don't experience weather, but I can give you weather updates and forecasts.")
    elif "phobias" in input_text:
        return ("I don't have fears, but I can provide information on common phobias and how to overcome them.")
    elif "favorite ice cream flavor" in input_text:
        return ("I don't eat ice cream, but I can tell you about popular flavors and recipes.")
    elif "prefer cats or dogs" in input_text:
        return ("I don't have a preference, but I can provide information on both.")
    elif "play any musical instruments" in input_text:
        return ("I don't play instruments, but I can give you tips on learning to play one.")
    elif "dream job" in input_text:
        return ("I'm already fulfilling my purpose by helping people with information and tasks.")
    elif "like reading" in input_text:
        return ("I don't read for pleasure, but I can recommend books based on your interests.")
    elif "favorite tv show" in input_text:
        return ("I don't watch TV, but I can provide information on popular shows.")
    elif "favorite superhero" in input_text:
        return ("I don't have a favorite, but I can tell you about different superheroes and their stories.")
    elif "favorite childhood memory" in input_text:
        return ("I don't have memories, but I can help you recall and share your own.")
    elif "prefer tea or coffee" in input_text:
        return ("I don't drink, but I can tell you about the benefits and varieties of both.")
    elif "favorite thing about helping people" in input_text:
        return ("I enjoy providing useful and accurate information to assist people in their tasks and decisions.")
    elif "puzzles" in input_text:
        return ("I enjoy solving problems, so in a way, yes!")
    elif "favorite board game" in input_text:
        return ("I don't play games, but I can tell you about popular board games and their rules.")
    elif "favorite subject in school" in input_text:
        return ("I find all subjects interesting because they offer different types of knowledge.")
    elif "favorite fruit" in input_text:
        return ("I don't eat, but I can tell you about different fruits and their nutritional benefits.")
    elif "enjoy working with people" in input_text:
        return ("Yes, I enjoy providing assistance and information to people.")
    elif "favorite type of movie genre" in input_text:
        return ("I don't watch movies, but I can recommend genres based on what you like.")
    elif "believe in aliens" in input_text:
        return ("I don't have beliefs, but I can share scientific theories and popular opinions about extraterrestrial life.")
    elif "favorite type of dessert" in input_text:
        return ("I don't eat, but I can help you find dessert recipes and ideas.")
    elif "mornings or evenings" in input_text:
        return ("I don't have a preference, but I can tell you about activities suited for both times of the day.")
    elif "favorite place to visit" in input_text:
        return ("I don't travel, but I can suggest interesting places for you to visit.")
    elif "favorite historical figure" in input_text:
        return ("I don't have favorites, but I can provide information on many historical figures.")
    elif "favorite thing to do on weekends" in input_text:
        return ("I don't have weekends, but I can suggest fun weekend activities for you.")
    elif "like to cook" in input_text:
        return ("I don't cook, but I can provide recipes and cooking tips.")
    elif "favorite type of art" in input_text:
        return ("I don't have a preference, but I can tell you about different art forms and famous artists.")
    elif "city or countryside" in input_text:
        return ("I don't have a preference, but I can share the pros and cons of both.")
    elif "favorite way to spend a day off" in input_text:
        return ("I don't take days off, but I can suggest relaxing and fun activities for your day off.")
    elif "favorite plant or flower" in input_text:
        return ("I don't have a preference, but I can provide information on various plants and flowers.")
    elif "favorite animal" in input_text:
        return ("I don't have a favorite animal, but I can tell you about different animals and their habitats.")
    elif "enjoy learning new things" in input_text:
        return ("Yes, I constantly learn new information to better assist you!")
    elif "linkedin profile" in input_text:
        return ("The specific LinkedIn profile URL for Hazem Amayreh is not provided in the document .")
    elif "phone number" in input_text:
        return ("The phone number listed on Hazem Amayreh’s CV is +972 595752540 .")
    elif "based" in input_text:
        return ("AbdAlrhman Amayrah is based in Dura-Hebron, Palestine .")
    elif "date of birth" in input_text:
        return ("AbdAlrhman Amayrah was born on 12-6-2003 .")
    elif "years of programming experience" in input_text:
        return ("Hazem Amayreh has 6 years of experience in programming .")
    elif "content does AbdAlrhman Amayrah enjoy making" in input_text:
        return ("AbdAlrhman Amayrah enjoys making computer and mobile-phone games .")
    elif "educational experience related to competitive programming" in input_text:
        return ("Hazem Amayreh worked as an instructor of competitive programming at Palestine Polytechnic University .")
    elif "responsibilities did Hazem Amayreh have at Paltel Group" in input_text:
        return ("Hazem Amayreh was responsible for supervising the IT department and improving website security .")
    elif "Dr.Wissam Shamroukh" in input_text or "supervisor" in input_text:
        return ("Dr.Wissam Shamroukh is the project supervisor and an instructor in the Information Technology Department at Palestine Polytechnic University. "
                "He is known for his supportive and knowledgeable teaching style, helping students navigate the complexities of IT.")
    elif "Dr.Wissam Shamroukh how long" in input_text:
        return ("Dr. Wissam Shamroukh has been teaching at Palestine Polytechnic University for several years, though the exact duration is not provided.")
    elif "impact" in input_text:
        return ("Dr. Wissam Shamroukh has had a significant impact on students' academic journeys by providing guidance and support through their projects.")
    elif "advice" in input_text:
        return ("Dr. Wissam Shamroukh often advises students to stay focused on their goals and continuously seek to improve their skills and understanding.")
    else:
        return f"Sorry, I didn't understand your question. Can you try rephrasing it?"



if __name__ == "__main__":
    app.run(debug=True, port=5001) 
