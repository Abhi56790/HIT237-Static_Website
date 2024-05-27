from django.shortcuts import render, get_object_or_404
from .models import ThesisProject

# Template render functions

def home(request):
    return render(request, 'as2_app/home.html')


def projectlist(request):
    projects = ThesisProject.objects.all()
    context = {
        'articles': projects,
    }
    return render(request, 'as2_app/projectlist.html', context)

def about(request):
    return render(request, 'as2_app/about.html')


def project_details(request , pk):
    
    

    selected_project = get_object_or_404(ThesisProject, pk=pk)

    #for proj in thess_projects:
        #if pk == proj.id:
           # selected_project = proj
          #  break


    context = {
        'project': selected_project,
    }

    return render(request, 'as2_app/projectdetails.html', context)



















# Local Function and class to store data


#def projects():
#
#    project_list = []
#
#    project_list.append(thesis_projects(1,
#                                        1,
#                                        'Machine learning approaches for Cyber Security',
#                                        'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction andfor an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
#                                        'Bharanidharan Shanmugam',
#                                        'Utilizing machine learning techniques to enhance cyber security by analyzing vast amounts of data for improved risk modeling and decision support.',
#                                       ))
#    
#    project_list.append(thesis_projects(2,
#                                        9,
#                                        'Informetrics applications in multidisciplinary domain',
#                                        'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniqueson various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary researchliterature using various machine learning, network analysis, data visualisation and data wrangling tools.',
#                                        'Yakub Sebastian',
#                                        'Exploring informetric properties of multidisciplinary research literature through the integration of machine learning, network analysis, data visualization, and data wrangling techniques.',
#                                        ))
#    
#    project_list.append(thesis_projects(3,
#                                        16,
#                                        'Development of a Virtual Reality System to Test Binaural Hearing',
#                                        'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design,implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
#                                        'Sami Azam',
#                                        'Developing and assessing a virtual reality system for objective testing of human binaural hearing abilities, utilizing common off-the-shelf components and programming techniques.',
#                                        ))
#    
#    project_list.append(thesis_projects(4,
#                                        41,
#                                        'Current trends on cryptomining and its potential impact on cryptocurrencies',
#                                        "Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computersand spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put thesoftware which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead ofrunning them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of thatwebsite. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies anddevelop a solution that can fulfil the gap. It also aims to find out:• What type crypto mining methodologies are being applied?• Apart from crypto-mining, what other security risks may it introduce? For example: cryptojacking• How current web standards are tackling this problem?",
#                                        'Sami Azam',
#                                        'Investigating the rising trend of website-based crypto-mining, identifying security risks like cryptojacking, and developing solutions to address gaps in current methodologies and web standards.',
#                                        ))
#    
#    project_list.append(thesis_projects(5,
#                                        176,
#                                        'Artificial Intelligence in Health Informatics',
#                                        'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.',
#                                        'Asif Karim',
#                                        'Leveraging various publicly available health datasets, this project aims to create an enhanced dataset through feature engineering, subsequently employing both traditional and deep learning algorithms to construct predictive models for health outcomes, with comparative analysis against existing research.',
#                                        ))
#    
#    project_list.append(thesis_projects(6,
#                                        180,
#                                        'Unsupervised Model Development from Autism Screening Data ',
#                                        'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests.',
#                                        'Asif Karim',
#                                        'Developing a cluster-based system to categorize toddlers based on medical traits, supported by thorough literature review, and validated through external and internal measures alongside statistical tests.',
#                                        ))
#    
#    project_list.append(thesis_projects(7,
#                                        226,
#                                        'Applying Artificial Intelligence to solve real world problems',
#                                        'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
#                                        'Bharanidharan Shanmugam',
#                                        'Exploring diverse applications of Artificial Intelligence with minimal human intervention, ranging from building bots to predicting power usage, across academia and industry.',
#                                        ))
#    
#    return project_list
#
#
#
#
#class thesis_projects:
#
#    def __init__(self, id, topic_num, title, description, superviser, relv_desc):
#
#        self.id = id
#        self.topic_num = topic_num
#        self.title = title
#        self.description = description
#        self.superviser = superviser
#        self.relv_desc = relv_desc
#
#
#    
#
#
#
#
# 