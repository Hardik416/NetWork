from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

@require_http_methods(["GET"])
def job_searching(request):
    return render(request, 'network_jobs/job_searching.html')

@require_http_methods(["GET"])
def job_list(request):
    # Sample job data
    jobs = [
        {
            'id': 1,
            'title': 'Senior Software Engineer',
            'company': 'Google',
            'location': 'Mountain View, CA',
            'salary': '$150,000 - $200,000',
            'type': 'Full-time',
            'logo': '/static/images/google.png',
            'description': 'We are looking for a Senior Software Engineer to join our team...',
            'requirements': ['5+ years of experience', 'Strong Python skills', 'Bachelor\'s degree'],
            'responsibilities': ['Design and implement features', 'Mentor junior developers'],
            'companySize': '1000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 2,
            'title': 'Frontend Developer',
            'company': 'Meta',
            'location': 'Menlo Park, CA',
            'salary': '$120,000 - $160,000',
            'type': 'Full-time',
            'logo': '/static/images/meta.png',
            'description': 'Join our frontend team to build beautiful user interfaces...',
            'requirements': ['3+ years of frontend experience', 'React expertise'],
            'responsibilities': ['Develop new features', 'Build reusable components'],
            'companySize': '5000+ employees',
            'industry': 'Social Media'
        },
        {
            'id': 3,
            'title': 'DevOps Engineer',
            'company': 'Amazon',
            'location': 'Seattle, WA',
            'salary': '$140,000 - $190,000',
            'type': 'Full-time',
            'logo': '/static/images/amazon2.png',
            'description': 'Join Amazon\'s infrastructure team to build and maintain cloud services.',
            'requirements': [
                '4+ years of DevOps experience',
                'Strong knowledge of AWS',
                'Experience with CI/CD pipelines',
                'Proficiency in Python or Shell scripting'
            ],
            'responsibilities': [
                'Manage cloud infrastructure',
                'Automate deployment processes',
                'Monitor system performance',
                'Implement security best practices'
            ],
            'companySize': '15,000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 4,
            'title': 'iOS Developer',
            'company': 'Apple',
            'location': 'Cupertino, CA',
            'salary': '$145,000 - $195,000',
            'type': 'Full-time',
            'logo': '/static/images/apple.png',
            'description': 'Create innovative iOS applications for Apple\'s ecosystem.',
            'requirements': [
                '5+ years of iOS development',
                'Expert in Swift and Objective-C',
                'Experience with UIKit and SwiftUI',
                'Strong understanding of iOS architecture'
            ],
            'responsibilities': [
                'Develop new iOS features',
                'Optimize app performance',
                'Collaborate with design team',
                'Maintain code quality'
            ],
            'companySize': '8,000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 5,
            'title': 'Data Scientist',
            'company': 'Microsoft',
            'location': 'Redmond, WA',
            'salary': '$135,000 - $185,000',
            'type': 'Full-time',
            'logo': '/static/images/microsoft.png',
            'description': 'Join Microsoft\'s data science team to drive business insights.',
            'requirements': [
                '4+ years of data science experience',
                'Strong knowledge of Python and R',
                'Experience with machine learning',
                'Master\'s degree in Statistics or related field'
            ],
            'responsibilities': [
                'Develop predictive models',
                'Analyze large datasets',
                'Present findings to stakeholders',
                'Collaborate with engineering teams'
            ],
            'companySize': '12,000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 6,
            'title': 'UX Designer',
            'company': 'Adobe',
            'location': 'San Jose, CA',
            'salary': '$110k - $150k',
            'type': 'Full-time',
            'logo': '/static/images/adobe2.png',
            'description': 'Create intuitive and engaging user experiences for our creative software suite. You\'ll work closely with designers and developers to bring ideas to life.',
            'requirements': [
                '3+ years of UX design experience',
                'Strong portfolio demonstrating user-centered design',
                'Proficiency in design tools',
                'Experience with user research'
            ],
            'responsibilities': [
                'Conduct user research',
                'Create wireframes and prototypes',
                'Design user interfaces',
                'Test and iterate on designs'
            ],
            'companySize': '2000+ employees',
            'industry': 'Software'
        },
        {
            'id': 7,
            'title': 'UI Designer',
            'company': 'Netflix',
            'location': 'San Francisco, CA',
            'salary': '$100k - $140k',
            'type': 'Full-time',
            'logo': '/static/images/netflix.png',
            'description': 'Design beautiful and functional user interfaces for our streaming platform. You\'ll help shape the future of entertainment and user experience.',
            'requirements': [
                '2+ years of UI design experience',
                'Strong visual design skills',
                'Experience with design systems',
                'Knowledge of web technologies'
            ],
            'responsibilities': [
                'Create visual designs',
                'Develop design systems',
                'Collaborate with developers',
                'Ensure design consistency'
            ],
            'companySize': '500+ employees',
            'industry': 'Entertainment'
        },
        {
            'id': 8,
            'title': 'Product Designer',
            'company': 'Tesla',
            'location': 'San Francisco, CA',
            'salary': '$120k - $160k',
            'type': 'Full-time',
            'logo': '/static/images/tesla.png',
            'description': 'Join our product design team to create exceptional experiences for our electric vehicles and energy products. You\'ll work on features that impact millions of users worldwide.',
            'requirements': [
                '4+ years of product design experience',
                'Strong portfolio of shipped products',
                'Experience with user research',
                'Knowledge of design systems'
            ],
            'responsibilities': [
                'Design new product features',
                'Conduct user research',
                'Create prototypes',
                'Collaborate with cross-functional teams'
            ],
            'companySize': '3000+ employees',
            'industry': 'Automotive'
        },
        {
            'id': 9,
            'title': 'Digital Marketing Manager',
            'company': 'IBM',
            'location': 'Cambridge, MA',
            'salary': '$90k - $130k',
            'type': 'Full-time',
            'logo': '/static/images/ibm.png',
            'description': 'Lead our digital marketing efforts and drive growth through various online channels. You\'ll develop and execute strategies to increase brand awareness and customer acquisition.',
            'requirements': [
                '5+ years of digital marketing experience',
                'Strong analytical skills',
                'Experience with marketing automation',
                'Knowledge of SEO and SEM'
            ],
            'responsibilities': [
                'Develop marketing strategies',
                'Manage digital campaigns',
                'Analyze performance metrics',
                'Lead marketing team'
            ],
            'companySize': '1000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 10,
            'title': 'Content Strategist',
            'company': 'LinkedIn',
            'location': 'Sunnyvale, CA',
            'salary': '$95k - $135k',
            'type': 'Full-time',
            'logo': '/static/images/linkedin.png',
            'description': 'Create compelling content strategies that engage our professional community and drive business growth. You\'ll work across various content formats and channels.',
            'requirements': [
                '3+ years of content strategy experience',
                'Strong writing and editing skills',
                'Experience with content management systems',
                'Knowledge of SEO best practices'
            ],
            'responsibilities': [
                'Develop content strategies',
                'Create engaging content',
                'Manage content calendar',
                'Analyze content performance'
            ],
            'companySize': '8000+ employees',
            'industry': 'Professional Networking'
        },
        {
            'id': 11,
            'title': 'SEO Specialist',
            'company': 'Samsung',
            'location': 'Seattle, WA',
            'salary': '$80k - $120k',
            'type': 'Full-time',
            'logo': '/static/images/samsung.png',
            'description': 'Optimize our website and content for search engines to increase organic traffic and improve visibility. You\'ll work with content and development teams to implement SEO best practices.',
            'requirements': [
                '2+ years of SEO experience',
                'Strong analytical skills',
                'Knowledge of SEO tools',
                'Experience with technical SEO'
            ],
            'responsibilities': [
                'Conduct keyword research',
                'Optimize website content',
                'Monitor search rankings',
                'Implement SEO strategies'
            ],
            'companySize': '100+ employees',
            'industry': 'SEO Software'
        },
        {
            'id': 12,
            'title': 'Sales Manager',
            'company': 'Salesforce',
            'location': 'San Francisco, CA',
            'salary': '$120k - $180k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/00A1E0/FFFFFF?text=S',
            'description': 'Lead our sales team to drive revenue growth and build strong client relationships. You\'ll develop sales strategies and mentor team members to achieve targets.',
            'requirements': [
                '5+ years of sales experience',
                '2+ years of team leadership',
                'Strong negotiation skills',
                'Experience with CRM systems'
            ],
            'responsibilities': [
                'Develop sales strategies',
                'Lead sales team',
                'Build client relationships',
                'Achieve revenue targets'
            ],
            'companySize': '5000+ employees',
            'industry': 'CRM Software'
        },
        {
            'id': 13,
            'title': 'Business Development Representative',
            'company': 'Zoom',
            'location': 'San Jose, CA',
            'salary': '$70k - $100k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/2D8CFF/FFFFFF?text=Z',
            'description': 'Drive new business growth by identifying and closing opportunities with enterprise clients. You\'ll build relationships and deliver solutions that meet client needs.',
            'requirements': [
                '3+ years of sales experience',
                'Strong communication skills',
                'Experience with enterprise sales',
                'Knowledge of video conferencing solutions'
            ],
            'responsibilities': [
                'Identify new opportunities',
                'Build client relationships',
                'Present solutions',
                'Close deals'
            ],
            'companySize': '2000+ employees',
            'industry': 'Video Conferencing'
        },
        {
            'id': 14,
            'title': 'Financial Analyst',
            'company': 'Goldman Sachs',
            'location': 'New York, NY',
            'salary': '$85k - $120k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/000000/FFFFFF?text=GS',
            'description': 'Analyze financial data to provide insights and recommendations for business decisions. You\'ll work with various departments to support strategic initiatives.',
            'requirements': [
                '2+ years of financial analysis experience',
                'Strong Excel and financial modeling skills',
                'Knowledge of financial statements',
                'Bachelor\'s degree in Finance or related field'
            ],
            'responsibilities': [
                'Analyze financial data',
                'Create financial models',
                'Prepare reports',
                'Support strategic initiatives'
            ],
            'companySize': '30000+ employees',
            'industry': 'Financial Services'
        },
        {
            'id': 15,
            'title': 'Investment Banking Analyst',
            'company': 'JPMorgan Chase',
            'location': 'New York, NY',
            'salary': '$100k - $150k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/000000/FFFFFF?text=JPM',
            'description': 'Work on complex financial transactions and provide strategic advice to corporate clients. You\'ll be part of a team that shapes major business deals.',
            'requirements': [
                '3+ years of investment banking experience',
                'Strong financial modeling skills',
                'Knowledge of M&A and capital markets',
                'MBA or related advanced degree'
            ],
            'responsibilities': [
                'Work on M&A transactions',
                'Prepare pitch books',
                'Conduct financial analysis',
                'Manage client relationships'
            ],
            'companySize': '25000+ employees',
            'industry': 'Banking'
        },
        {
            'id': 16,
            'title': 'HR Manager',
            'company': 'Netflix',
            'location': 'Los Gatos, CA',
            'salary': '$110k - $160k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/E50914/FFFFFF?text=N',
            'description': 'Lead our HR team to create an exceptional employee experience and support our company\'s growth. You\'ll develop and implement HR strategies that align with our culture.',
            'requirements': [
                '5+ years of HR experience',
                '2+ years of team leadership',
                'Knowledge of HR best practices',
                'Experience with HR systems'
            ],
            'responsibilities': [
                'Develop HR strategies',
                'Lead HR team',
                'Manage employee relations',
                'Support company culture'
            ],
            'companySize': '2000+ employees',
            'industry': 'Entertainment'
        },
        {
            'id': 17,
            'title': 'Technical Recruiter',
            'company': 'Twitter',
            'location': 'San Francisco, CA',
            'salary': '$90k - $130k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/1DA1F2/FFFFFF?text=T',
            'description': 'Help us find and attract top talent to join our growing team. You\'ll work closely with hiring managers to identify needs and build strong candidate pipelines.',
            'requirements': [
                '2+ years of recruitment experience',
                'Strong sourcing skills',
                'Experience with ATS systems',
                'Knowledge of recruitment best practices'
            ],
            'responsibilities': [
                'Source candidates',
                'Screen applicants',
                'Conduct interviews',
                'Manage hiring process'
            ],
            'companySize': '1000+ employees',
            'industry': 'Social Media'
        },
        {
            'id': 18,
            'title': 'Customer Success Manager',
            'company': 'Zendesk',
            'location': 'San Francisco, CA',
            'salary': '$85k - $125k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/03363D/FFFFFF?text=Z',
            'description': 'Ensure our customers\' success by providing exceptional support and guidance. You\'ll work closely with customers to understand their needs and help them achieve their goals.',
            'requirements': [
                '2+ years of customer success experience',
                'Strong communication skills',
                'Experience with CRM systems',
                'Knowledge of customer support best practices'
            ],
            'responsibilities': [
                'Manage customer relationships',
                'Provide product guidance',
                'Handle customer inquiries',
                'Drive customer satisfaction'
            ],
            'companySize': '500+ employees',
            'industry': 'Customer Service Software'
        },
        {
            'id': 19,
            'title': 'Technical Support Engineer',
            'company': 'Atlassian',
            'location': 'Sydney, Australia',
            'salary': '$80k - $120k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/0052CC/FFFFFF?text=A',
            'description': 'Provide technical support to our customers and help them resolve complex issues. You\'ll work with various teams to ensure customer satisfaction and product improvement.',
            'requirements': [
                '3+ years of technical support experience',
                'Strong problem-solving skills',
                'Knowledge of software development',
                'Experience with support tools'
            ],
            'responsibilities': [
                'Resolve technical issues',
                'Document solutions',
                'Collaborate with development team',
                'Improve support processes'
            ],
            'companySize': '1000+ employees',
            'industry': 'Software'
        },
        {
            'id': 20,
            'title': 'Operations Manager',
            'company': 'Uber',
            'location': 'San Francisco, CA',
            'salary': '$100k - $150k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/000000/FFFFFF?text=U',
            'description': 'Oversee our operations to ensure efficient and effective service delivery. You\'ll work with various teams to optimize processes and improve performance.',
            'requirements': [
                '5+ years of operations experience',
                'Strong leadership skills',
                'Experience with process improvement',
                'Knowledge of operations management'
            ],
            'responsibilities': [
                'Manage operations team',
                'Optimize processes',
                'Monitor performance metrics',
                'Implement improvements'
            ],
            'companySize': '5000+ employees',
            'industry': 'Transportation'
        },
        {
            'id': 21,
            'title': 'Supply Chain Analyst',
            'company': 'Walmart',
            'location': 'Bentonville, AR',
            'salary': '$75k - $110k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/0071DC/FFFFFF?text=W',
            'description': 'Analyze and optimize our supply chain operations to improve efficiency and reduce costs. You\'ll work with various stakeholders to implement improvements.',
            'requirements': [
                '3+ years of supply chain experience',
                'Strong analytical skills',
                'Knowledge of supply chain management',
                'Experience with data analysis'
            ],
            'responsibilities': [
                'Analyze supply chain data',
                'Identify optimization opportunities',
                'Implement improvements',
                'Monitor performance'
            ],
            'companySize': '10000+ employees',
            'industry': 'E-commerce'
        },
        {
            'id': 22,
            'title': 'Corporate Counsel',
            'company': 'Tesla',
            'location': 'Austin, TX',
            'salary': '$150k - $200k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/CC0000/FFFFFF?text=T',
            'description': 'Provide legal guidance and support for our business operations. You\'ll work on various legal matters and help ensure compliance with regulations.',
            'requirements': [
                '5+ years of legal experience',
                'JD degree and bar admission',
                'Experience with corporate law',
                'Knowledge of technology law'
            ],
            'responsibilities': [
                'Provide legal counsel',
                'Review contracts',
                'Ensure compliance',
                'Manage legal matters'
            ],
            'companySize': '5000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 23,
            'title': 'Legal Operations Manager',
            'company': 'Stripe',
            'location': 'San Francisco, CA',
            'salary': '$120k - $170k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/6772E5/FFFFFF?text=S',
            'description': 'Streamline our legal operations and implement efficient processes. You\'ll work with the legal team to optimize workflows and improve productivity.',
            'requirements': [
                '3+ years of legal operations experience',
                'Strong project management skills',
                'Knowledge of legal technology',
                'Experience with process improvement'
            ],
            'responsibilities': [
                'Optimize legal processes',
                'Implement legal technology',
                'Manage legal projects',
                'Improve team efficiency'
            ],
            'companySize': '1000+ employees',
            'industry': 'Technology'
        },
        {
            'id': 24,
            'title': 'Research Scientist',
            'company': 'OpenAI',
            'location': 'San Francisco, CA',
            'salary': '$180k - $250k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/412991/FFFFFF?text=O',
            'description': 'Conduct cutting-edge research in artificial intelligence and machine learning. You\'ll work on innovative projects that push the boundaries of what\'s possible.',
            'requirements': [
                'PhD in Computer Science or related field',
                'Strong research background',
                'Experience with AI/ML',
                'Published research papers'
            ],
            'responsibilities': [
                'Conduct research',
                'Develop new algorithms',
                'Publish papers',
                'Collaborate with research team'
            ],
            'companySize': '500+ employees',
            'industry': 'Artificial Intelligence'
        },
        {
            'id': 25,
            'title': 'AI Research Engineer',
            'company': 'DeepMind',
            'location': 'London, UK',
            'salary': '$160k - $220k',
            'type': 'Full-time',
            'logo': 'https://via.placeholder.com/80/000000/FFFFFF?text=D',
            'description': 'Work on advanced AI research projects and help develop the next generation of AI systems. You\'ll collaborate with world-class researchers and engineers.',
            'requirements': [
                '3+ years of AI research experience',
                'Strong programming skills',
                'Knowledge of machine learning',
                'Experience with deep learning'
            ],
            'responsibilities': [
                'Develop AI systems',
                'Conduct experiments',
                'Write research papers',
                'Collaborate with team'
            ],
            'companySize': '200+ employees',
            'industry': 'Artificial Intelligence'
        }
    ]

    # Get the page number from the request
    page = request.GET.get('page', 1)
    
    # Create a paginator object
    paginator = Paginator(jobs, 5)  # Show 5 jobs per page
    
    try:
        # Get the jobs for the requested page
        jobs_page = paginator.page(page)
    except:
        # If page is not an integer or out of range, deliver first page
        jobs_page = paginator.page(1)

    # If it's an AJAX request, return JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'jobs': list(jobs_page),
            'has_next': jobs_page.has_next(),
            'has_previous': jobs_page.has_previous(),
            'current_page': jobs_page.number,
            'total_pages': paginator.num_pages,
            'total_jobs': paginator.count,
            'jobs_per_page': 5,
            'filters': {
                'industries': list(set(job['industry'] for job in jobs)),
                'locations': list(set(job['location'] for job in jobs)),
                'jobTypes': list(set(job['type'] for job in jobs)),
                'experienceLevels': list(set(job.get('experienceLevel', '') for job in jobs))
            }
        })

    # For regular requests, render the template
    template_name = 'network_jobs/job_list.html'
    return render(request, template_name, {
        'jobs': jobs_page,
        'total_pages': paginator.num_pages,
        'total_jobs': paginator.count,
        'jobs_per_page': 5,
        'filters': {
            'industries': list(set(job['industry'] for job in jobs)),
            'locations': list(set(job['location'] for job in jobs)),
            'jobTypes': list(set(job['type'] for job in jobs)),
            'experienceLevels': list(set(job.get('experienceLevel', '') for job in jobs))
        }
    })

@require_http_methods(["POST"])
def apply_for_job(request):
    try:
        data = json.loads(request.body)
        job_id = data.get('jobId')
        # Here you would typically:
        # 1. Validate the job exists
        # 2. Check if user is authenticated
        # 3. Process the application
        # 4. Store in database
        # 5. Send confirmation email
        
        return JsonResponse({
            'status': 'success',
            'message': 'Application submitted successfully',
            'jobId': job_id
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@require_http_methods(["GET"])
def get_job_details(request, job_id):
    # In a real application, you would fetch this from a database
    # This is just a sample response
    job_details = {
        'id': job_id,
        'title': 'Senior Software Engineer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': '$150k - $200k',
        'type': 'Full-time',
        'logo': 'https://via.placeholder.com/80/4285F4/FFFFFF?text=G',
        'description': 'We are looking for a Senior Software Engineer to join our team...',
        'requirements': [
            '5+ years of experience in software development',
            'Strong knowledge of Python, Java, or C++',
            'Experience with distributed systems',
            'Bachelor\'s degree in Computer Science or related field'
        ],
        'responsibilities': [
            'Design and implement new features',
            'Mentor junior developers',
            'Participate in code reviews',
            'Collaborate with cross-functional teams'
        ],
        'companySize': '1000+ employees',
        'industry': 'Technology',
        'postedDate': '2024-03-15',
        'applicationDeadline': '2024-04-15',
        'benefits': [
            'Competitive salary and equity',
            'Comprehensive health coverage',
            '401(k) matching',
            'Flexible work arrangements'
        ],
        'skills': ['Python', 'Java', 'C++', 'Distributed Systems', 'Cloud Computing'],
        'experienceLevel': 'Senior',
        'education': 'Bachelor\'s Degree',
        'remotePolicy': 'Hybrid'
    }
    
    return JsonResponse(job_details)

@login_required
@require_http_methods(["GET", "POST"])
def post_job(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # Here you would typically save the job to your database
            # For now, we'll just return a success message
            return JsonResponse({
                "status": "success",
                "message": "Job posted successfully",
                "job": data
            })
        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON data"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
    
    # GET request - render the job posting form
    return render(request, 'network_jobs/job_posting.html')
