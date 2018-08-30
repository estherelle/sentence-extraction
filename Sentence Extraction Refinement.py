{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "from collections import OrderedDict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"http://www.elevate-hr.com/about-us/\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "# perform GET request to target url\n",
    "r = requests.get(url)\n",
    "s = BeautifulSoup(r.text, \"lxml\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "# s.getText(separator=u' ');\n",
    "\n",
    "# # get contents in <body> tag\n",
    "# bod = s.find('body')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "# substitute extra whitespace with single newline\n",
    "bod_sub = re.sub(r'(\\t|\\n|\\s)*\\n(\\t|\\n|\\s)*', '\\n\\n',s.getText(separator=u' '))\n",
    "# strip trailing whitespace\n",
    "bod_sub = bod_sub.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "bod_sub;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [],
   "source": [
    "# replace newlines\n",
    "# bod_stripped = bod_sub.replace('(.|!|?)\\n', '. ')\n",
    "bod_stripped = bod_sub.replace('.\\n', '. ')\n",
    "bod_stripped = bod_stripped.replace('!\\n', '. ')\n",
    "bod_stripped = bod_stripped.replace('Inc.', 'Incorporated')\n",
    "bod_stripped = bod_stripped.replace('?\\n', '. ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'About Elevate HR\\n\\nvar sf_appPath=\\'/\\';\\n\\n(function(i,s,o,g,r,a,m){i[\\'GoogleAnalyticsObject\\']=r;i[r]=i[r]||function(){\\n\\n(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\\n\\nm=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\\n\\n})(window,document,\\'script\\',\\'https://www.google-analytics.com/analytics.js\\',\\'ga\\');\\n\\nga(\\'create\\', \\'UA-61208428-1\\', \\'auto\\');\\n\\nga(\\'send\\', \\'pageview\\');\\n\\n/* about page mobile background */\\n\\njQuery(document).ready(function(){\\n\\nfunction applyBgfit(){\\n\\nvar height = jQuery(\\'.video-block.inner\\').height();\\n\\njQuery(\\'.section.about-page.about-david-section\\').css({\"margin-bottom\": height/2 + 50, \"padding-bottom\": height/2});\\n\\n}\\n\\napplyBgfit();\\n\\njQuery(window).resize(applyBgfit);\\n\\n})\\n\\n.posistion-tag{\\n\\ntop:-40px !important;\\n\\n}\\n\\n.posistion-tag-sol {\\n\\npadding-bottom: 30px;\\n\\nposition: absolute;\\n\\ntop: 0px;\\n\\n}\\n\\n.header.section .navbar-default .navbar-nav li:hover ul li a:hover {\\n\\ncolor: #0a884b;\\n\\n}\\n\\n.btn:hover {\\n\\ncolor: #0a884b !important;\\n\\nbackground: white !important;\\n\\nborder: 2px solid #0a884b !important;\\n\\nbackground-color: white !important;\\n\\nheight: 45px !important;\\n\\n}\\n\\nToggle navigation\\n\\nSolutions\\n\\nD365 for Talent\\n\\nActive Directory Integration\\n\\nD365 ERP HCM\\n\\nDynamics AX 2012 HCM\\n\\nSolution Features\\n\\nServices\\n\\nHR Process Consulting\\n\\nSystem Implementation Consulting\\n\\nCustomer Care\\n\\nShop\\n\\nAbout Us\\n\\nStory\\n\\nValues\\n\\nLeadership\\n\\nNews + Events\\n\\nNews\\n\\nEvents\\n\\nTrade Shows\\n\\nResources\\n\\nWhite Papers and Fact Sheets\\n\\nWebinars and Videos\\n\\nCareers\\n\\nContact Us\\n\\nSearch\\n\\n.active {\\n\\nborder-bottom: 2px solid #2D9761 !important;\\n\\n}\\n\\nul.nav > li a{font-weight:bold !important;}\\n\\n$(document).ready(function () {\\n\\n$(\\'ul.nav li.dropdown\\').hover(function () {\\n\\n$(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeIn(100);\\n\\n}, function () {\\n\\n$(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeOut(100);\\n\\n});\\n\\nvar pathName = location.pathname.split(\"/\")[1];\\n\\nif(pathName != \"\"){\\n\\n$(\\'ul.nav > li > a[href^=\"/\\' + location.pathname.split(\"/\")[1] + \\'\"]\\').addClass(\\'active\\');\\n\\n}\\n\\n});\\n\\nWe Are Elevate HR\\n\\nElevate HR, Incorporated is the world’s preeminent, dedicated provider of Human Capital Management (HCM) solutions and\\xa0implementation services for Microsoft Dynamics 365 for Talent, and Finance & Operations. \\nOur Story\\n\\nElevate HR was formed in 2009 from the Dynamics AX practice of MindKey A/S, the Danish company who wrote the original Dynamics AX HCM modules under contract to Microsoft. Our legacy of delivering exceptional service and results to global Dynamics AX HCM clients since the software platform’s inception in 1998 anchors our status as the world\\'s top partner for Microsoft Dynamics 365 for Talent, as well as for Finance & Operations HCM solutions. \\nA History of Microsoft Dynamics © \\xa0 365 + Elevate HR, Inc\\n\\nOur Relationship with Microsoft Elevate HR’s heritage as developer of the original HCM modules in Dynamics 365, from the product’s inception as Axapta through its Dynamics AX years, gives us both a long history and a close ongoing relationship with Microsoft. We share a mission to empower all people, and deliver tools to help your talent achieve the very best. Our roadmap aligns with Microsoft’s roadmap so that our stream of new products will continue to boost the functionality of Talent in Dynamics 365 for years to come. \\nOur Role as An ISV Elevate HR is an Independent Software Vendor (ISV), emblematic of Microsoft’s ISV strategy. Microsoft Dynamics is global in capability, broad in application, advanced in its technical core, and fully integrated with the entire Microsoft technology stack. Microsoft invites ISV’s into the Dynamics platform to ensure that, in addition to the breadth offered by Microsoft, customers also have the most advanced and contemporary functional depth provided by Elevate HR. \\nThe Elevate HR Difference\\n\\nElevate HR is known for the unrivalled quality and precision of its software products and for the unparalleled depth of our knowledge in Human Resource and Payroll business processes, Human Capital Management Technology, and Business Transformation. We work directly with Customers to implement the full HCM solution, and also deliver support to our Microsoft Partners as \"the Partner\\'s Partner\" for all HCM solutions. We remain closely aligned with Microsoft on product development to ensure that our offering adds value over the long run, that our products are current with Dynamics 365 for Talent, and for Finance & Operations updates and releases, and that we remain focused on our customers’ needs for Dynamics 365 HCM software products. \\nOur Values\\n\\nOur\\n\\nvalues of Teamwork, Honesty, Respect, Communication, and Loyalty describe how\\n\\nwe work with our customers, and with each other.\\xa0 We work together with\\n\\nyou, tell it like it is, treat everyone as we expect to be treated, share\\n\\ninformation you need to know, and earn your loyalty. \\nOur Culture Elevate HR reinforces its\\xa0storied legacy and trusted brand with a\\n\\nvibrant start-up culture.\\xa0 Every member\\n\\nof the Elevate HR team receives license to realize the full range of their\\n\\ntalent, push boundaries and drive our business forward in exciting, unexpected\\n\\ndirections. \\nWe Are Unique We revolutionize traditional Human Resources with invigorating resources  for  humans. Elevate HR solutions and services are designed with you in mind, to enhance and conserve  your  two most valuable resources: talent and time. \\nHow We Think & Who We Are We are all colleagues at Elevate HR. From our\\n\\nproduct designers and software engineers to our consultants, solutions\\n\\narchitects, and administrative staff, everyone here and everyone we hire are\\n\\ndynamic contributors to our values and our successes. \\nAbout David Erickson, Founder + CEO\\n\\nDavid M. Erickson, CEO, Elevate HR, Incorporated has spent the past 30 years in strategic, senior executive roles in HR technology, operations, business transformation, and development. He served as CEO of MindKey Global A/S prior to founding Elevate HR in 2009. David played central leadership roles at Pfizer, Bristol-Myers Squibb, and Honeywell International, through three of the largest corporate mergers in history. He has advised senior business leaders on business transformation, Human Resources strategy and solutions for companies as varied as Hewlett-Packard, Lucent, the United Nations, and Wachovia. David is a frequent conference speaker, and has been invited by IHRIM, SHRM and other professional societies and industry consortiums in Europe, Asia, and North America to speak on such topics as shared services, human capital analytics, HR technology, enterprise portals, and business transformation. \\nHow can we help you. \\nCONTACT US Shop. \\nToggle navigation\\n\\nPrivacy Policy\\n\\nResources\\n\\nSolutions\\n\\n.active {\\n\\nborder-bottom: 2px solid #2D9761 !important;\\n\\n}\\n\\nul.nav > li a{font-weight:bold !important;}\\n\\n$(document).ready(function () {\\n\\n$(\\'ul.nav li.dropdown\\').hover(function () {\\n\\n$(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeIn(100);\\n\\n}, function () {\\n\\n$(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeOut(100);\\n\\n});\\n\\nvar pathName = location.pathname.split(\"/\")[1];\\n\\nif(pathName != \"\"){\\n\\n$(\\'ul.nav > li > a[href^=\"/\\' + location.pathname.split(\"/\")[1] + \\'\"]\\').addClass(\\'active\\');\\n\\n}\\n\\n});\\n\\n© 2018 Elevate HR, Incorporated'"
      ]
     },
     "execution_count": 99,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bod_stripped"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [],
   "source": [
    "# takes care of sentences that dont' end with periods- extra newline blocks were\n",
    "# replaced by a single newline in line 15\n",
    "bod_s = re.sub(r'(([a-z])|([A-Z]))+\\n(([a-z])|([A-Z]))+', ' ',bod_stripped)\n",
    "stripped_newlines = bod_s.replace('\\n\\n', '. ')\n",
    "stripped_newlines = bod_s.replace('\\n', ' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'About Elevate HR  var sf_appPath=\\'/\\';  (function(i,s,o,g,r,a,m){i[\\'GoogleAnalyticsObject\\']=r;i[r]=i[r]||function(){  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)  })(window,document,\\'script\\',\\'https://www.google-analytics.com/analytics.js\\',\\'ga\\');  ga(\\'create\\', \\'UA-61208428-1\\', \\'auto\\');  ga(\\'send\\', \\'pageview\\');  /* about page mobile background */  jQuery(document).ready(function(){  function applyBgfit(){  var height = jQuery(\\'.video-block.inner\\').height();  jQuery(\\'.section.about-page.about-david-section\\').css({\"margin-bottom\": height/2 + 50, \"padding-bottom\": height/2});  }  applyBgfit();  jQuery(window).resize(applyBgfit);  })  .posistion-tag{  top:-40px !important;  }  .posistion-tag-sol {  padding-bottom: 30px;  position: absolute;  top: 0px;  }  .header.section .navbar-default .navbar-nav li:hover ul li a:hover {  color: #0a884b;  }  .btn:hover {  color: #0a884b !important;  background: white !important;  border: 2px solid #0a884b !important;  background-color: white !important;  height: 45px !important;  }  Toggle navigation  Solutions  D365 for Talent  Active Directory Integration  D365 ERP HCM  Dynamics AX 2012 HCM  Solution Features  Services  HR Process Consulting  System Implementation Consulting  Customer Care  Shop  About Us  Story  Values  Leadership  News + Events  News  Events  Trade Shows  Resources  White Papers and Fact Sheets  Webinars and Videos  Careers  Contact Us  Search  .active {  border-bottom: 2px solid #2D9761 !important;  }  ul.nav > li a{font-weight:bold !important;}  $(document).ready(function () {  $(\\'ul.nav li.dropdown\\').hover(function () {  $(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeIn(100);  }, function () {  $(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeOut(100);  });  var pathName = location.pathname.split(\"/\")[1];  if(pathName != \"\"){  $(\\'ul.nav > li > a[href^=\"/\\' + location.pathname.split(\"/\")[1] + \\'\"]\\').addClass(\\'active\\');  }  });  We Are Elevate HR  Elevate HR, Incorporated is the world’s preeminent, dedicated provider of Human Capital Management (HCM) solutions and\\xa0implementation services for Microsoft Dynamics 365 for Talent, and Finance & Operations.  Our Story  Elevate HR was formed in 2009 from the Dynamics AX practice of MindKey A/S, the Danish company who wrote the original Dynamics AX HCM modules under contract to Microsoft. Our legacy of delivering exceptional service and results to global Dynamics AX HCM clients since the software platform’s inception in 1998 anchors our status as the world\\'s top partner for Microsoft Dynamics 365 for Talent, as well as for Finance & Operations HCM solutions.  A History of Microsoft Dynamics © \\xa0 365 + Elevate HR, Inc  Our Relationship with Microsoft Elevate HR’s heritage as developer of the original HCM modules in Dynamics 365, from the product’s inception as Axapta through its Dynamics AX years, gives us both a long history and a close ongoing relationship with Microsoft. We share a mission to empower all people, and deliver tools to help your talent achieve the very best. Our roadmap aligns with Microsoft’s roadmap so that our stream of new products will continue to boost the functionality of Talent in Dynamics 365 for years to come.  Our Role as An ISV Elevate HR is an Independent Software Vendor (ISV), emblematic of Microsoft’s ISV strategy. Microsoft Dynamics is global in capability, broad in application, advanced in its technical core, and fully integrated with the entire Microsoft technology stack. Microsoft invites ISV’s into the Dynamics platform to ensure that, in addition to the breadth offered by Microsoft, customers also have the most advanced and contemporary functional depth provided by Elevate HR.  The Elevate HR Difference  Elevate HR is known for the unrivalled quality and precision of its software products and for the unparalleled depth of our knowledge in Human Resource and Payroll business processes, Human Capital Management Technology, and Business Transformation. We work directly with Customers to implement the full HCM solution, and also deliver support to our Microsoft Partners as \"the Partner\\'s Partner\" for all HCM solutions. We remain closely aligned with Microsoft on product development to ensure that our offering adds value over the long run, that our products are current with Dynamics 365 for Talent, and for Finance & Operations updates and releases, and that we remain focused on our customers’ needs for Dynamics 365 HCM software products.  Our Values  Our  values of Teamwork, Honesty, Respect, Communication, and Loyalty describe how  we work with our customers, and with each other.\\xa0 We work together with  you, tell it like it is, treat everyone as we expect to be treated, share  information you need to know, and earn your loyalty.  Our Culture Elevate HR reinforces its\\xa0storied legacy and trusted brand with a  vibrant start-up culture.\\xa0 Every member  of the Elevate HR team receives license to realize the full range of their  talent, push boundaries and drive our business forward in exciting, unexpected  directions.  We Are Unique We revolutionize traditional Human Resources with invigorating resources  for  humans. Elevate HR solutions and services are designed with you in mind, to enhance and conserve  your  two most valuable resources: talent and time.  How We Think & Who We Are We are all colleagues at Elevate HR. From our  product designers and software engineers to our consultants, solutions  architects, and administrative staff, everyone here and everyone we hire are  dynamic contributors to our values and our successes.  About David Erickson, Founder + CEO  David M. Erickson, CEO, Elevate HR, Incorporated has spent the past 30 years in strategic, senior executive roles in HR technology, operations, business transformation, and development. He served as CEO of MindKey Global A/S prior to founding Elevate HR in 2009. David played central leadership roles at Pfizer, Bristol-Myers Squibb, and Honeywell International, through three of the largest corporate mergers in history. He has advised senior business leaders on business transformation, Human Resources strategy and solutions for companies as varied as Hewlett-Packard, Lucent, the United Nations, and Wachovia. David is a frequent conference speaker, and has been invited by IHRIM, SHRM and other professional societies and industry consortiums in Europe, Asia, and North America to speak on such topics as shared services, human capital analytics, HR technology, enterprise portals, and business transformation.  How can we help you.  CONTACT US Shop.  Toggle navigation  Privacy Policy  Resources  Solutions  .active {  border-bottom: 2px solid #2D9761 !important;  }  ul.nav > li a{font-weight:bold !important;}  $(document).ready(function () {  $(\\'ul.nav li.dropdown\\').hover(function () {  $(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeIn(100);  }, function () {  $(this).find(\\'.dropdown-menu\\').stop(true, true).delay(200).fadeOut(100);  });  var pathName = location.pathname.split(\"/\")[1];  if(pathName != \"\"){  $(\\'ul.nav > li > a[href^=\"/\\' + location.pathname.split(\"/\")[1] + \\'\"]\\').addClass(\\'active\\');  }  });  © 2018 Elevate HR, Incorporated'"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stripped_newlines"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "# strip any remaining trailing whitespace (probably unnecessary)\n",
    "stripped_newlines = stripped_newlines.strip()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "stripped_newlines;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "# split by sentences and add back period at the end of each sentence\n",
    "stripped = stripped_newlines.split('.')\n",
    "stripped = [(strip + '.') for strip in stripped]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "stripped;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "cleaned = []\n",
    "\n",
    "stopwords = [\"function\", \"{\", \"}\", \"https\", \"http\", \"href\", \");\", \"javascript\", \"return\", \"async\", \"]\", \"crossorigin\", \"error\", \"js\", \"()\", \"var \", \"*\", \"invoked\", \"\\\"/\\\"\"]\n",
    "for strip in stripped:\n",
    "    separated = strip.split(' ')\n",
    "    if len(separated) > 3:\n",
    "        stopped = False\n",
    "        for stopword in stopwords:\n",
    "            if stopword in strip:\n",
    "                stopped = True\n",
    "                break\n",
    "        if not stopped:\n",
    "            cleaned.append(strip)\n",
    "\n",
    "# text, arr = get_sentences(\"https://asana.com/company\")\n",
    "# print(text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Our Story  Elevate HR was formed in 2009 from the Dynamics AX practice of MindKey A/S, the Danish company who wrote the original Dynamics AX HCM modules under contract to Microsoft.',\n",
       " \"Our legacy of delivering exceptional service and results to global Dynamics AX HCM clients since the software platform’s inception in 1998 anchors our status as the world's top partner for Microsoft Dynamics 365 for Talent, as well as for Finance & Operations HCM solutions.\",\n",
       " 'A History of Microsoft Dynamics © \\xa0 365 + Elevate HR, Inc  Our Relationship with Microsoft Elevate HR’s heritage as developer of the original HCM modules in Dynamics 365, from the product’s inception as Axapta through its Dynamics AX years, gives us both a long history and a close ongoing relationship with Microsoft.',\n",
       " 'We share a mission to empower all people, and deliver tools to help your talent achieve the very best.',\n",
       " 'Our Role as An ISV Elevate HR is an Independent Software Vendor (ISV), emblematic of Microsoft’s ISV strategy.',\n",
       " 'Microsoft Dynamics is global in capability, broad in application, advanced in its technical core, and fully integrated with the entire Microsoft technology stack.',\n",
       " 'The Elevate HR Difference  Elevate HR is known for the unrivalled quality and precision of its software products and for the unparalleled depth of our knowledge in Human Resource and Payroll business processes, Human Capital Management Technology, and Business Transformation.',\n",
       " 'We work directly with Customers to implement the full HCM solution, and also deliver support to our Microsoft Partners as \"the Partner\\'s Partner\" for all HCM solutions.',\n",
       " 'We remain closely aligned with Microsoft on product development to ensure that our offering adds value over the long run, that our products are current with Dynamics 365 for Talent, and for Finance & Operations updates and releases, and that we remain focused on our customers’ needs for Dynamics 365 HCM software products.',\n",
       " 'Our Values  Our  values of Teamwork, Honesty, Respect, Communication, and Loyalty describe how  we work with our customers, and with each other.',\n",
       " 'We work together with  you, tell it like it is, treat everyone as we expect to be treated, share  information you need to know, and earn your loyalty.',\n",
       " 'Our Culture Elevate HR reinforces its\\xa0storied legacy and trusted brand with a  vibrant start-up culture.',\n",
       " 'Every member  of the Elevate HR team receives license to realize the full range of their  talent, push boundaries and drive our business forward in exciting, unexpected  directions.',\n",
       " 'We Are Unique We revolutionize traditional Human Resources with invigorating resources  for  humans.',\n",
       " 'Elevate HR solutions and services are designed with you in mind, to enhance and conserve  your  two most valuable resources: talent and time.',\n",
       " 'How We Think & Who We Are We are all colleagues at Elevate HR.',\n",
       " 'From our  product designers and software engineers to our consultants, solutions  architects, and administrative staff, everyone here and everyone we hire are  dynamic contributors to our values and our successes.',\n",
       " 'About David Erickson, Founder + CEO  David M.',\n",
       " 'Erickson, CEO, Elevate HR, Incorporated has spent the past 30 years in strategic, senior executive roles in HR technology, operations, business transformation, and development.',\n",
       " 'He served as CEO of MindKey Global A/S prior to founding Elevate HR in 2009.',\n",
       " 'David played central leadership roles at Pfizer, Bristol-Myers Squibb, and Honeywell International, through three of the largest corporate mergers in history.',\n",
       " 'He has advised senior business leaders on business transformation, Human Resources strategy and solutions for companies as varied as Hewlett-Packard, Lucent, the United Nations, and Wachovia.',\n",
       " 'David is a frequent conference speaker, and has been invited by IHRIM, SHRM and other professional societies and industry consortiums in Europe, Asia, and North America to speak on such topics as shared services, human capital analytics, HR technology, enterprise portals, and business transformation.',\n",
       " 'How can we help you.',\n",
       " 'CONTACT US Shop.',\n",
       " 'Toggle navigation  Privacy Policy  Resources  Solutions  .']"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cleaned"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:py36]",
   "language": "python",
   "name": "conda-env-py36-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
