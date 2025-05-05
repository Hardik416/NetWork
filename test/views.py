from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@require_http_methods(["GET"])
def job_list(request):
    # Comprehensive sample job data with detailed information
    jobs = [
        # Technology Jobs
        {
            'id': 1,
            'title': 'Senior Software Engineer',
            'company': 'Google',
            'location': 'Mountain View, CA',
            'salary': '$150k - $200k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60',
            'description': 'We are looking for a Senior Software Engineer to join our team and help build the next generation of our platform. You will be working on complex technical challenges and mentoring junior developers.',
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
        },
        {
            'id': 2,
            'title': 'Frontend Developer',
            'company': 'Meta',
            'location': 'Remote',
            'salary': '$120k - $160k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 3,
            'title': 'DevOps Engineer',
            'company': 'Amazon',
            'location': 'Seattle, WA',
            'salary': '$130k - $180k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 4,
            'title': 'iOS Developer',
            'company': 'Apple',
            'location': 'Cupertino, CA',
            'salary': '$140k - $190k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 5,
            'title': 'Data Scientist',
            'company': 'Microsoft',
            'location': 'Redmond, WA',
            'salary': '$130k - $180k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Design Jobs
        {
            'id': 6,
            'title': 'UX Designer',
            'company': 'Adobe',
            'location': 'San Jose, CA',
            'salary': '$100k - $150k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 7,
            'title': 'UI Designer',
            'company': 'Figma',
            'location': 'San Francisco, CA',
            'salary': '$90k - $140k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 8,
            'title': 'Product Designer',
            'company': 'Airbnb',
            'location': 'Remote',
            'salary': '$110k - $160k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Marketing Jobs
        {
            'id': 9,
            'title': 'Digital Marketing Manager',
            'company': 'HubSpot',
            'location': 'Cambridge, MA',
            'salary': '$90k - $130k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 10,
            'title': 'Content Strategist',
            'company': 'LinkedIn',
            'location': 'Sunnyvale, CA',
            'salary': '$85k - $120k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 11,
            'title': 'SEO Specialist',
            'company': 'Moz',
            'location': 'Remote',
            'salary': '$70k - $100k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Sales Jobs
        {
            'id': 12,
            'title': 'Sales Manager',
            'company': 'Salesforce',
            'location': 'San Francisco, CA',
            'salary': '$100k - $150k + Commission',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 13,
            'title': 'Account Executive',
            'company': 'Zoom',
            'location': 'San Jose, CA',
            'salary': '$80k - $120k + Commission',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Finance Jobs
        {
            'id': 14,
            'title': 'Financial Analyst',
            'company': 'Goldman Sachs',
            'location': 'New York, NY',
            'salary': '$90k - $130k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 15,
            'title': 'Investment Banker',
            'company': 'JPMorgan Chase',
            'location': 'New York, NY',
            'salary': '$120k - $180k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # HR Jobs
        {
            'id': 16,
            'title': 'HR Manager',
            'company': 'Netflix',
            'location': 'Los Gatos, CA',
            'salary': '$100k - $150k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 17,
            'title': 'Talent Acquisition Specialist',
            'company': 'Twitter',
            'location': 'San Francisco, CA',
            'salary': '$80k - $120k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Customer Service Jobs
        {
            'id': 18,
            'title': 'Customer Success Manager',
            'company': 'Zendesk',
            'location': 'Remote',
            'salary': '$70k - $100k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 19,
            'title': 'Support Engineer',
            'company': 'Atlassian',
            'location': 'Remote',
            'salary': '$80k - $110k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Operations Jobs
        {
            'id': 20,
            'title': 'Operations Manager',
            'company': 'Uber',
            'location': 'San Francisco, CA',
            'salary': '$90k - $140k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 21,
            'title': 'Supply Chain Analyst',
            'company': 'Amazon',
            'location': 'Seattle, WA',
            'salary': '$80k - $120k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Legal Jobs
        {
            'id': 22,
            'title': 'Corporate Counsel',
            'company': 'Facebook',
            'location': 'Menlo Park, CA',
            'salary': '$150k - $200k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 23,
            'title': 'Legal Operations Manager',
            'company': 'Google',
            'location': 'Mountain View, CA',
            'salary': '$120k - $160k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },

        # Research Jobs
        {
            'id': 24,
            'title': 'Research Scientist',
            'company': 'DeepMind',
            'location': 'London, UK',
            'salary': '$130k - $180k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
        },
        {
            'id': 25,
            'title': 'AI Research Engineer',
            'company': 'OpenAI',
            'location': 'San Francisco, CA',
            'salary': '$140k - $190k',
            'type': 'Full-time',
            'logo': '/api/placeholder/60/60'
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
                'experienceLevels': list(set(job['experienceLevel'] for job in jobs))
            }
        })

    # For regular requests, render the template
    return render(request, 'test/job-list.html', {
        'jobs': jobs_page,
        'total_pages': paginator.num_pages,
        'total_jobs': paginator.count,
        'jobs_per_page': 5,
        'filters': {
            'industries': list(set(job['industry'] for job in jobs)),
            'locations': list(set(job['location'] for job in jobs)),
            'jobTypes': list(set(job['type'] for job in jobs)),
            'experienceLevels': list(set(job['experienceLevel'] for job in jobs))
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
        'logo': '/api/placeholder/60/60',
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
    return render(request, 'test/post-job.html') 