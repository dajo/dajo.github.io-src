#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jason Lachowsky'
NAME = u'Jason Lachowsky'
SITENAME = u'Jason Lachowsky'
SITEURL = ''
TAGLINE = u'Serial skill-gatherer'
EMAIL = u'jason@lachowsky.com'
PHONE = u'612 702 5171'
TWITTER = u'@jlachowsky'
GITHUB = u'dajo'
LINKEDIN = u'lachowsky'
PATH = 'content'

EXPERIENCES = [
	{
		'job_title': 'Director of Information Systems',
		'time': 'Sep 2016 - June 2017',
		'company': 'Minnesota Senate, St. Paul, MN',
		'details': '<ul><li>Managed a diverse staff of seven, reorganized into three units: IT Services, Systems, and Development</li> <li>Catalyzed continuous improvement throughout organization; guided adoption of new technologies; implemented improved identity and access management and SSO through ADFS 3.0 for Office 365</li> <li>Prioritized which internal applications to redevelop, improve, fix, cease development of, or abandon; used JIRA to formalize SDLC of existing and new applications; shared future roadmap with leadership</li> <li>Orchestrated IT onboarding efforts of new Senate majority and newly-elected Senators including extensive moving and secondary offices; formalized service offerings</li> <li>Pioneered use of an internal Knowledge Base for technical documentation as well as a How-to library for end users; When possible, resolved tickets linked to the relevant KB article</li> <li>Instituted IT Service Management (ITSM) model offering a standardized method to record and track work using Atlassian products and ITIL methodology; modeled processes for service desk work</li> <li>Created first formal efforts at soliciting feedback from end users, discussing changes through a committee structure, and organizing groups of beta testers</li> <li>Deployed private and public WiFi network for the MN Capitol Building, including 150+ wireless access points (WAPs); participated in wireless survey; devised security protocols</li> <li>Pitched alternate network topology for Capitol renovation, resulting in $20k savings due to more economical SFPs; network topology included 2 core rooms funneling connectivity to 17 closets</li> <li>Managed vendor relationships, support contracts, and maintenance costs; deduplicated when beneficial </li> <li>Facilitated joint efforts between development and other IT staff (DevOps) to improve software delivery; guided implementation of BitBucket as first version control server and Bamboo for release management</li></ul>'	
	},
	{
		'job_title': 'Infrastructure Engineer',
		'time': 'Nov 2015 - Sep 2016',
		'company': 'Minnesota Senate, St. Paul, MN',
		'details': '<ul><li>Planned transition from Novell OES to Microsoft Active Directory; devised scripts to aid in conversion</li> <li>Proposed low-cost in-place upgrade of workstation base; devised method to ensure minimal downtime</li> <li>Built robust load-balanced Ubuntu Linux servers for websites and internal/external database connections; saved costs by changing database backend from MS SQL to MySQL.</li> <li>Formalized vCenter Server virtualization with enforced templates; migrated to C-series Cisco UCS rack server, integrated this with Nimble hybrid flash storage array</li> <li>Centralized logging from as many devices as possible into a syslog-ng instance; logs were then forwarded to a Splunk instance for monitoring and analysis</li> <li>Instrumental in the network design and deployment at new building including 22 switches and 37 WAPs</li> <li>Manage wired and wireless network; maintained 99.993% uptime during tenure</li> <li>Dispatched application updating mechanism and enabled remote support capability for over 350 workstations; technicians could support Senators in their home districts</li> <li>Evaluated, then executed modern solutions for IP address tracking and enterprise password management, replacing poorly-maintained text files</li> </ul>'
	},
	{
		'job_title': 'Web Content Manager',
		'time': 'Jan 2014 to Nov 2015',
		'company': 'Dakota County Technical College/Inver Hills Community College, Rosemount, MN',
		'details': '<ul><li>Maintained and developed two higher education websites and applications through shared services</li> <li>Used version control system to collaborate with back-end developers</li> <li>Recommended potential efficiencies, optimized content for voice, readability and search engines</li> <li>Collaborated and planned with department faculty to share unique features of each academic program</li> <li>Queried, joined and interpreted proprietary data with SQL for use in web applications</li></ul>'	
	},
	{
		'job_title': 'Interactive Marketing Manager',
		'time': 'Mar 2011 to Dec 2013',
		'company': 'Inver Hills Community College, Inver Grove Heights, MN',
		'details': '<ul><li>Devised principal features of redesigned website (wireframes, information architecture, content norms)</li> <li>Spearheaded effort to replace EOL content management system and migrate to a newer CMS</li> <li>Implemented campus-wide calendar/events system in use by academics, admissions, and student life</li> <li>Managed e-Marketing budget; completed ~5 targeted online advertising campaigns annually</li> <li>Mentored employees in own department; supervised student employee; served on faculty searches </li></ul>'
	},
	{
		'job_title': 'Web Content Developer',
		'time': 'Mar 2007 to Feb 2011',
		'company': 'Inver Hills Community College, Inver Grove Heights, MN',
		'details': '<ul><li>Developed several key college websites including Admissions, Library, Online Courses, and Orientation </li> <li>Wrote new content and refined existing content to ensure a fresh, clear and consistent voice </li> <li>Instituted and maintained social network presence including YouTube, LinkedIn, Facebook, and Twitter</li> <li>Led technology seminars and presentations at student events and faculty development days </li> <li>Offered adjunct teaching position in Innovation Technology and Instruction department</li> <li>Created/sourced graphic imagery as needed; directed/produced videos used in new student orientation</li></ul>'
	},
	{
		'job_title': 'Freelance Web Designer / Contractor',
		'time': 'Sep 2005 to Mar 2007',
		'company': 'Cognate, St. Paul, MN',
		'details': '<ul><li>Developed over 35 commercial and non-profit websites via proposal and contract work</li> <li>Cultivated entrepreneurial initiative by targeting local businesses and offering web marketing services</li> <li>Demonstrated project management skills; handled all aspects of web production including training</li></ul>'
	},
	{
		'job_title': 'Web Developer I',
		'time': 'Feb 2003 to Sep 2005',
		'company': 'Designstein, Inc., Minneapolis, MN',
		'details': '<ul><li>Created websites based on client requirements, prototyped web designs and information architecture</li> <li>Trained clients in web best practices and set up basic content management systems</li></ul>'
	},
	{
		'job_title': 'Operations & Special Projects',
		'time': 'Dec 2001 to Feb 2003',
		'company': 'Open Systems International, Inc., Plymouth, MN',
		'details': '<ul><li>Developed project-based time recording system for company of 75 employees; created reports </li> <li>Responded to help desk tickets as informal member of the IT department; built systems for new employees</li></ul>'
	},
	{
		'job_title': 'Web Technology Intern',
		'time': 'Summers 1999-2001',
		'company': 'Hennepin County: Environmental Services, Minneapolis, MN',
		'details': '<ul><li>Revised departmental website to meet external audience needs and ensure Sect. 508 compliance</li> <li>Developed and implemented an internal Intranet site; composed all content</li></ul>'
	},
	{
		'job_title': 'Student Web Designer',
		'time': 'Acad. Year 1999-2002',
		'company': 'University of Minnesota, Morris, Morris, MN',
		'details': '<ul><li>While employed at the Center for Small Towns, created web presences for rural MN communities</li> <li>Developed or improved several University websites for academic and student service departments</li></ul>'
	}
	
]

EDUCATIONS = [
	{
		'degree': 'M.S., Management of Technology',
		'meta': 'Technological Leadership Institute<br />University of Minnesota',
		'time': 'Fall 2017 - Spr 2019'
	},
	{
		'degree': 'B.A., English (GPA 3.3)',
		'meta': 'Minor: French/Philosophy<br />Univ. of Minnesota, Morris',
		'time': 'Fall 1998 - Sum 2002'
	},
	{
		'degree': 'B.A.S., Information Assurance (GPA 3.9)',
		'meta': 'Metropolitan State University',
		'time': 'Spr 2015 - Fall 2017'
	},
	{
		'degree': 'A.A.S., Network Technology and Security (GPA 3.9)',
		'meta': 'Inver Hills Community College',
		'time': 'Fall 2014 - Fall 2017'
	},
	{
		'degree': 'A.S., Contemporary Business (GPA 4.0)',
		'meta': 'Inver Hills Community College',
		'time': 'Fall 2012 - Fall 2013'
	},
	{
		'degree': 'Certificate, Project Management',
		'meta': 'Inver Hills Community College',
		'time': 'May 2013'
	},
	{
		'degree': 'Certificate, Supervision',
		'meta': 'Inver Hills Community College',
		'time': 'Dec 2013'
	},
	{
		'degree': 'High School Diploma',
		'meta': 'St. Paul Central High School',
		'time': 'Fall 1994 - Spring 1998'
	}
]


SKILLS = [
	{
		'title': 'Networking',
   		'level': '75'
   	},
	{
		'title': 'Security',
   		'level': '75'
   	},
  	{
  		'title': 'Windows Administration',
   		'level': '65'
   	},
    {
  		'title': 'Linux Administration',
  		'level': '50'
  	},
  	{
  		'title': 'PHP',
  		'level': '40'
  	},
  	{
  		'title': 'Python',
  		'level': '30'
  	},
  	{
  		'title': 'SQL',
  		'level': '30'
  	}
]

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "../pelican-themes/resume"