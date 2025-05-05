// Sample job details data (in a real app, this would come from the backend)
const jobDetails = {
    1: {
        description: "We are looking for a Senior Software Engineer to join our team and help build the next generation of our platform. You will be working on complex technical challenges and mentoring junior developers.",
        requirements: [
            "5+ years of experience in software development",
            "Strong knowledge of Python, Java, or C++",
            "Experience with distributed systems",
            "Bachelor's degree in Computer Science or related field"
        ],
        responsibilities: [
            "Design and implement new features",
            "Mentor junior developers",
            "Participate in code reviews",
            "Collaborate with cross-functional teams"
        ],
        companySize: "1000+ employees",
        industry: "Technology"
    },
    2: {
        description: "Join our frontend team to build beautiful, responsive, and performant user interfaces. You'll work with modern frameworks and tools to create exceptional user experiences.",
        requirements: [
            "3+ years of frontend development experience",
            "Expertise in React, Vue, or Angular",
            "Strong CSS and JavaScript skills",
            "Experience with responsive design"
        ],
        responsibilities: [
            "Develop new user-facing features",
            "Build reusable components",
            "Optimize applications for performance",
            "Collaborate with UX/UI designers"
        ],
        companySize: "5000+ employees",
        industry: "Social Media"
    },
    3: {
        description: "As a DevOps Engineer, you'll be responsible for maintaining and improving our cloud infrastructure, implementing CI/CD pipelines, and ensuring system reliability.",
        requirements: [
            "4+ years of DevOps experience",
            "Strong knowledge of AWS or Azure",
            "Experience with Docker and Kubernetes",
            "Proficiency in infrastructure as code"
        ],
        responsibilities: [
            "Manage cloud infrastructure",
            "Implement automated deployment pipelines",
            "Monitor system performance",
            "Ensure security best practices"
        ],
        companySize: "10000+ employees",
        industry: "E-commerce"
    },
    4: {
        description: "Join our iOS team to create innovative and user-friendly mobile applications. You'll work on cutting-edge features and help shape the future of mobile technology.",
        requirements: [
            "4+ years of iOS development",
            "Strong Swift and Objective-C skills",
            "Experience with iOS frameworks",
            "Published apps in the App Store"
        ],
        responsibilities: [
            "Develop new iOS features",
            "Optimize app performance",
            "Collaborate with design team",
            "Maintain code quality"
        ],
        companySize: "8000+ employees",
        industry: "Technology"
    },
    5: {
        description: "Work with large datasets to extract insights and build machine learning models that drive business decisions. You'll collaborate with cross-functional teams to solve complex problems.",
        requirements: [
            "3+ years of data science experience",
            "Strong Python and SQL skills",
            "Experience with machine learning frameworks",
            "Advanced degree in Statistics or related field"
        ],
        responsibilities: [
            "Develop predictive models",
            "Analyze complex datasets",
            "Present findings to stakeholders",
            "Collaborate on data-driven solutions"
        ],
        companySize: "15000+ employees",
        industry: "Technology"
    },
    6: {
        description: "Create intuitive and engaging user experiences for our creative software suite. You'll work closely with designers and developers to bring ideas to life.",
        requirements: [
            "3+ years of UX design experience",
            "Strong portfolio demonstrating user-centered design",
            "Proficiency in design tools",
            "Experience with user research"
        ],
        responsibilities: [
            "Conduct user research",
            "Create wireframes and prototypes",
            "Design user interfaces",
            "Test and iterate on designs"
        ],
        companySize: "2000+ employees",
        industry: "Software"
    },
    7: {
        description: "Design beautiful and functional user interfaces for our collaborative design platform. You'll help shape the future of design tools and workflows.",
        requirements: [
            "2+ years of UI design experience",
            "Strong visual design skills",
            "Experience with design systems",
            "Knowledge of web technologies"
        ],
        responsibilities: [
            "Create visual designs",
            "Develop design systems",
            "Collaborate with developers",
            "Ensure design consistency"
        ],
        companySize: "500+ employees",
        industry: "Design Tools"
    },
    8: {
        description: "Join our product design team to create exceptional experiences for our global community. You'll work on features that impact millions of users worldwide.",
        requirements: [
            "4+ years of product design experience",
            "Strong portfolio of shipped products",
            "Experience with user research",
            "Knowledge of design systems"
        ],
        responsibilities: [
            "Design new product features",
            "Conduct user research",
            "Create prototypes",
            "Collaborate with cross-functional teams"
        ],
        companySize: "3000+ employees",
        industry: "Travel"
    },
    9: {
        description: "Lead our digital marketing efforts and drive growth through various online channels. You'll develop and execute strategies to increase brand awareness and customer acquisition.",
        requirements: [
            "5+ years of digital marketing experience",
            "Strong analytical skills",
            "Experience with marketing automation",
            "Knowledge of SEO and SEM"
        ],
        responsibilities: [
            "Develop marketing strategies",
            "Manage digital campaigns",
            "Analyze performance metrics",
            "Lead marketing team"
        ],
        companySize: "1000+ employees",
        industry: "Marketing Software"
    },
    10: {
        description: "Create compelling content strategies that engage our professional community and drive business growth. You'll work across various content formats and channels.",
        requirements: [
            "3+ years of content strategy experience",
            "Strong writing and editing skills",
            "Experience with content management systems",
            "Knowledge of SEO best practices"
        ],
        responsibilities: [
            "Develop content strategies",
            "Create engaging content",
            "Manage content calendar",
            "Analyze content performance"
        ],
        companySize: "8000+ employees",
        industry: "Professional Networking"
    },
    11: {
        description: "Optimize our website and content for search engines to increase organic traffic and improve visibility. You'll work with content and development teams to implement SEO best practices.",
        requirements: [
            "2+ years of SEO experience",
            "Strong analytical skills",
            "Knowledge of SEO tools",
            "Experience with technical SEO"
        ],
        responsibilities: [
            "Conduct keyword research",
            "Optimize website content",
            "Monitor search rankings",
            "Implement SEO strategies"
        ],
        companySize: "100+ employees",
        industry: "SEO Software"
    },
    12: {
        description: "Lead our sales team to drive revenue growth and build strong client relationships. You'll develop sales strategies and mentor team members to achieve targets.",
        requirements: [
            "5+ years of sales experience",
            "2+ years of team leadership",
            "Strong negotiation skills",
            "Experience with CRM systems"
        ],
        responsibilities: [
            "Develop sales strategies",
            "Lead sales team",
            "Build client relationships",
            "Achieve revenue targets"
        ],
        companySize: "5000+ employees",
        industry: "CRM Software"
    },
    13: {
        description: "Drive new business growth by identifying and closing opportunities with enterprise clients. You'll build relationships and deliver solutions that meet client needs.",
        requirements: [
            "3+ years of sales experience",
            "Strong communication skills",
            "Experience with enterprise sales",
            "Knowledge of video conferencing solutions"
        ],
        responsibilities: [
            "Identify new opportunities",
            "Build client relationships",
            "Present solutions",
            "Close deals"
        ],
        companySize: "2000+ employees",
        industry: "Video Conferencing"
    },
    14: {
        description: "Analyze financial data to provide insights and recommendations for business decisions. You'll work with various departments to support strategic initiatives.",
        requirements: [
            "2+ years of financial analysis experience",
            "Strong Excel and financial modeling skills",
            "Knowledge of financial statements",
            "Bachelor's degree in Finance or related field"
        ],
        responsibilities: [
            "Analyze financial data",
            "Create financial models",
            "Prepare reports",
            "Support strategic initiatives"
        ],
        companySize: "30000+ employees",
        industry: "Financial Services"
    },
    15: {
        description: "Work on complex financial transactions and provide strategic advice to corporate clients. You'll be part of a team that shapes major business deals.",
        requirements: [
            "3+ years of investment banking experience",
            "Strong financial modeling skills",
            "Knowledge of M&A and capital markets",
            "MBA or related advanced degree"
        ],
        responsibilities: [
            "Work on M&A transactions",
            "Prepare pitch books",
            "Conduct financial analysis",
            "Manage client relationships"
        ],
        companySize: "25000+ employees",
        industry: "Banking"
    },
    16: {
        description: "Lead our HR team to create an exceptional employee experience and support our company's growth. You'll develop and implement HR strategies that align with our culture.",
        requirements: [
            "5+ years of HR experience",
            "2+ years of team leadership",
            "Knowledge of HR best practices",
            "Experience with HR systems"
        ],
        responsibilities: [
            "Develop HR strategies",
            "Lead HR team",
            "Manage employee relations",
            "Support company culture"
        ],
        companySize: "2000+ employees",
        industry: "Entertainment"
    },
    17: {
        description: "Help us find and attract top talent to join our growing team. You'll work closely with hiring managers to identify needs and build strong candidate pipelines.",
        requirements: [
            "2+ years of recruitment experience",
            "Strong sourcing skills",
            "Experience with ATS systems",
            "Knowledge of recruitment best practices"
        ],
        responsibilities: [
            "Source candidates",
            "Screen applicants",
            "Conduct interviews",
            "Manage hiring process"
        ],
        companySize: "1000+ employees",
        industry: "Social Media"
    },
    18: {
        description: "Ensure our customers' success by providing exceptional support and guidance. You'll work closely with customers to understand their needs and help them achieve their goals.",
        requirements: [
            "2+ years of customer success experience",
            "Strong communication skills",
            "Experience with CRM systems",
            "Knowledge of customer support best practices"
        ],
        responsibilities: [
            "Manage customer relationships",
            "Provide product guidance",
            "Handle customer inquiries",
            "Drive customer satisfaction"
        ],
        companySize: "500+ employees",
        industry: "Customer Service Software"
    },
    19: {
        description: "Provide technical support to our customers and help them resolve complex issues. You'll work with various teams to ensure customer satisfaction and product improvement.",
        requirements: [
            "3+ years of technical support experience",
            "Strong problem-solving skills",
            "Knowledge of software development",
            "Experience with support tools"
        ],
        responsibilities: [
            "Resolve technical issues",
            "Document solutions",
            "Collaborate with development team",
            "Improve support processes"
        ],
        companySize: "1000+ employees",
        industry: "Software"
    },
    20: {
        description: "Oversee our operations to ensure efficient and effective service delivery. You'll work with various teams to optimize processes and improve performance.",
        requirements: [
            "5+ years of operations experience",
            "Strong leadership skills",
            "Experience with process improvement",
            "Knowledge of operations management"
        ],
        responsibilities: [
            "Manage operations team",
            "Optimize processes",
            "Monitor performance metrics",
            "Implement improvements"
        ],
        companySize: "5000+ employees",
        industry: "Transportation"
    },
    21: {
        description: "Analyze and optimize our supply chain operations to improve efficiency and reduce costs. You'll work with various stakeholders to implement improvements.",
        requirements: [
            "3+ years of supply chain experience",
            "Strong analytical skills",
            "Knowledge of supply chain management",
            "Experience with data analysis"
        ],
        responsibilities: [
            "Analyze supply chain data",
            "Identify optimization opportunities",
            "Implement improvements",
            "Monitor performance"
        ],
        companySize: "10000+ employees",
        industry: "E-commerce"
    },
    22: {
        description: "Provide legal guidance and support for our business operations. You'll work on various legal matters and help ensure compliance with regulations.",
        requirements: [
            "5+ years of legal experience",
            "JD degree and bar admission",
            "Experience with corporate law",
            "Knowledge of technology law"
        ],
        responsibilities: [
            "Provide legal counsel",
            "Review contracts",
            "Ensure compliance",
            "Manage legal matters"
        ],
        companySize: "5000+ employees",
        industry: "Technology"
    },
    23: {
        description: "Streamline our legal operations and implement efficient processes. You'll work with the legal team to optimize workflows and improve productivity.",
        requirements: [
            "3+ years of legal operations experience",
            "Strong project management skills",
            "Knowledge of legal technology",
            "Experience with process improvement"
        ],
        responsibilities: [
            "Optimize legal processes",
            "Implement legal technology",
            "Manage legal projects",
            "Improve team efficiency"
        ],
        companySize: "1000+ employees",
        industry: "Technology"
    },
    24: {
        description: "Conduct cutting-edge research in artificial intelligence and machine learning. You'll work on innovative projects that push the boundaries of what's possible.",
        requirements: [
            "PhD in Computer Science or related field",
            "Strong research background",
            "Experience with AI/ML",
            "Published research papers"
        ],
        responsibilities: [
            "Conduct research",
            "Develop new algorithms",
            "Publish papers",
            "Collaborate with research team"
        ],
        companySize: "500+ employees",
        industry: "Artificial Intelligence"
    },
    25: {
        description: "Work on advanced AI research projects and help develop the next generation of AI systems. You'll collaborate with world-class researchers and engineers.",
        requirements: [
            "3+ years of AI research experience",
            "Strong programming skills",
            "Knowledge of machine learning",
            "Experience with deep learning"
        ],
        responsibilities: [
            "Develop AI systems",
            "Conduct experiments",
            "Write research papers",
            "Collaborate with team"
        ],
        companySize: "200+ employees",
        industry: "Artificial Intelligence"
    }
};

// Add click handlers for job cards
document.querySelectorAll('.job-card').forEach(card => {
    card.addEventListener('click', function() {
        const jobId = this.dataset.jobId;
        const job = jobDetails[jobId] || {
            description: "Detailed job description coming soon...",
            requirements: ["Requirements will be listed here"],
            responsibilities: ["Responsibilities will be listed here"],
            companySize: "Company size information",
            industry: "Industry information"
        };

        // Update modal content
        document.getElementById('modal-logo').src = this.querySelector('.company-logo').src;
        document.getElementById('modal-title').textContent = this.querySelector('.job-title').textContent;
        document.getElementById('modal-company').textContent = this.querySelector('.company-name').textContent;
        document.getElementById('modal-location').textContent = this.querySelector('.job-meta-item:nth-child(1)').textContent;
        document.getElementById('modal-salary').textContent = this.querySelector('.job-meta-item:nth-child(2)').textContent;
        document.getElementById('modal-type').textContent = this.querySelector('.job-meta-item:nth-child(3)').textContent;
        document.getElementById('modal-description').textContent = job.description;
        document.getElementById('modal-company-size').textContent = job.companySize;
        document.getElementById('modal-industry').textContent = job.industry;

        // Update requirements
        const requirementsList = document.getElementById('modal-requirements');
        requirementsList.innerHTML = job.requirements.map(req => `<li>${req}</li>`).join('');

        // Update responsibilities
        const responsibilitiesList = document.getElementById('modal-responsibilities');
        responsibilitiesList.innerHTML = job.responsibilities.map(resp => `<li>${resp}</li>`).join('');

        // Show modal
        document.querySelector('.modal-overlay').classList.add('active');
    });
});

// Close modal when clicking the close button or outside the modal
document.querySelector('.modal-close').addEventListener('click', closeModal);
document.querySelector('.modal-overlay').addEventListener('click', function(e) {
    if (e.target === this) {
        closeModal();
    }
});

function closeModal() {
    document.querySelector('.modal-overlay').classList.remove('active');
}

// Apply button handler
document.querySelector('.apply-btn-large').addEventListener('click', function() {
    alert('Application submitted successfully!');
    closeModal();
});

// Add click handlers for pagination
document.querySelectorAll('.page-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const page = this.dataset.page;
        if (page) {
            loadJobs(page);
        }
    });
});

function loadJobs(page) {
    // Show loading state
    document.querySelector('.job-list').innerHTML = '<div class="loading">Loading jobs...</div>';
    
    // Fetch jobs for the requested page
    fetch(`/jobs/?page=${page}`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Update the job list
        const jobList = document.querySelector('.job-list');
        jobList.innerHTML = data.jobs.map(job => `
            <div class="job-card" data-job-id="${job.id}">
                <div class="company-logo-container">
                    <img src="${job.logo}" 
                         alt="${job.company}" 
                         class="company-logo">
                </div>
                <div class="job-info">
                    <h3 class="job-title">${job.title}</h3>
                    <div class="company-name">${job.company}</div>
                    <div class="job-meta">
                        <span class="job-meta-item">📍 ${job.location}</span>
                        <span class="job-meta-item">💰 ${job.salary}</span>
                        <span class="job-meta-item">⏰ ${job.type}</span>
                    </div>
                </div>
            </div>
        `).join('');

        // Update pagination
        updatePagination(data);

        // Reattach event listeners
        attachEventListeners();
    })
    .catch(error => {
        console.error('Error loading jobs:', error);
        document.querySelector('.job-list').innerHTML = '<div class="error">Error loading jobs. Please try again.</div>';
    });
}

function updatePagination(data) {
    const pagination = document.querySelector('.pagination');
    let paginationHTML = '';

    if (data.has_previous) {
        paginationHTML += `<button class="page-btn" data-page="${data.current_page - 1}">Previous</button>`;
    }

    for (let i = 1; i <= data.total_pages; i++) {
        if (i === data.current_page) {
            paginationHTML += `<button class="page-btn active">${i}</button>`;
        } else {
            paginationHTML += `<button class="page-btn" data-page="${i}">${i}</button>`;
        }
    }

    if (data.has_next) {
        paginationHTML += `<button class="page-btn" data-page="${data.current_page + 1}">Next</button>`;
    }

    pagination.innerHTML = paginationHTML;
}

function attachEventListeners() {
    // Reattach job card click handlers
    document.querySelectorAll('.job-card').forEach(card => {
        card.addEventListener('click', function() {
            const jobId = this.dataset.jobId;
            const job = jobDetails[jobId] || {
                description: "Detailed job description coming soon...",
                requirements: ["Requirements will be listed here"],
                responsibilities: ["Responsibilities will be listed here"],
                companySize: "Company size information",
                industry: "Industry information"
            };

            // Update modal content
            document.getElementById('modal-logo').src = this.querySelector('.company-logo').src;
            document.getElementById('modal-title').textContent = this.querySelector('.job-title').textContent;
            document.getElementById('modal-company').textContent = this.querySelector('.company-name').textContent;
            document.getElementById('modal-location').textContent = this.querySelector('.job-meta-item:nth-child(1)').textContent;
            document.getElementById('modal-salary').textContent = this.querySelector('.job-meta-item:nth-child(2)').textContent;
            document.getElementById('modal-type').textContent = this.querySelector('.job-meta-item:nth-child(3)').textContent;
            document.getElementById('modal-description').textContent = job.description;
            document.getElementById('modal-company-size').textContent = job.companySize;
            document.getElementById('modal-industry').textContent = job.industry;

            // Update requirements
            const requirementsList = document.getElementById('modal-requirements');
            requirementsList.innerHTML = job.requirements.map(req => `<li>${req}</li>`).join('');

            // Update responsibilities
            const responsibilitiesList = document.getElementById('modal-responsibilities');
            responsibilitiesList.innerHTML = job.responsibilities.map(resp => `<li>${resp}</li>`).join('');

            // Show modal
            document.querySelector('.modal-overlay').classList.add('active');
        });
    });

    // Reattach pagination handlers
    document.querySelectorAll('.page-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const page = this.dataset.page;
            if (page) {
                loadJobs(page);
            }
        });
    });
}
