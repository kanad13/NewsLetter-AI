import streamlit as st

config = {'scrollZoom': True, 'displayModeBar': True, 'displaylogo': False}
st.set_page_config(page_title="News Letters", page_icon=":chat-plus-outline:", layout="wide", initial_sidebar_state="expanded", menu_items=None)
st.write("""
### Sample Documents for NewsLetter.AI

To showcase how NewsLetter.AI works with Generative AI on custom documents, I created fictional NewsLetters for 4 departments viz. Sales, Networks, COPS & IT.

The chatbot answers questions based on these newsletters.\n

So for example, if an employee wants to know what are "current month's customer satisfaction scores", then they can just ask the chatbot that question and get the answer using the power of Generative AI.

#### All Documents Supported

Beyond newsletters, Newsletter.AI effortlessly processes any document type out-of-the-box.

Just input your reports, memos, or manuals, and receive relevant responses powered by Generative AI.

You just need to place them in the [input_files folder](https://github.com/kanad13/NewsLetter-AI/tree/main/input_files).\n

#### No code changes needed

No code changes needed to the chatbot. The chatbot starts providing answers based on latest information.\n

This is on account of the **intelligent hash-based cache management** implemented in NewsLetter.AI.

You can find more details - [here](https://github.com/kanad13/NewsLetter-AI/tree/main?tab=readme-ov-file#what-sets-newsletterai-apart)

#### Text of all NewsLetters

**This section shows the contents of all NewsLetters that act as an input for the AI.**

=============== 01-COPS Newsletter - September 2024.txt ===============

**Operational Updates**

- **Performance Metrics**: We are pleased to report that our average customer satisfaction score for September was 92%, exceeding our target of 90%. Our average handling time (AHT) for customer calls was 4 minutes and 22 seconds, a 10% improvement from July.
- **New Process**: Starting this month, we are implementing a new workflow for handling fiber installation requests. This change aims to reduce the average time to install by 2 days. Training sessions for the new process will be held on October 12th and 15th.

**Customer Insights**

- **Customer Feedback**: Our customers have been praising our technical support team for their patience and expertise. One customer wrote, "The tech support agent was very knowledgeable and helped me resolve my issue quickly. Thank you!"
- **Common Issues**: We have noticed an increase in calls about data usage limits. To address this, we are updating our FAQs and training our frontline staff to provide clearer explanations of our data plans.

**Service Updates**

- **New Product Launch**: We are excited to announce the launch of our new 5G mobile plan, offering faster speeds and larger data allowances. Training on the new plan will be provided to all customer-facing staff.
- **Network Upgrades**: Our network operations team will be performing maintenance on our fiber network on October 20th, which may cause brief outages. We will notify affected customers in advance.

**Employee Spotlight**

- **Employee of the Month**: Congratulations to Jane Doe from our technical support team for her outstanding performance and dedication to customer satisfaction. Jane consistently receives positive feedback from customers and colleagues alike.
- **Best Practices**: This month, we are highlighting the best practices of our billing team, who have implemented a new process for handling billing inquiries that has reduced resolution time by 30%.

**Training and Development**

- **Upcoming Training**: On October 22nd, we will be offering a training session on advanced troubleshooting techniques for mobile services. All customer-facing staff are encouraged to attend.
- **Learning and Development**: Our L&D team has launched a new e-learning module on customer service skills. This module is available on our intranet and is mandatory for all new hires.

**Industry News**

- **Regulatory Update**: The telecom regulator has announced new guidelines for customer data protection. We are reviewing these guidelines and will implement necessary changes to our processes.
- **Market Trends**: The latest market research shows an increase in demand for fiber-to-the-home services. We are well-positioned to meet this demand with our expanding fiber network.

**Technology Corner**

- **New Tool**: We are introducing a new CRM tool to help manage customer interactions more efficiently. Training on this tool will be provided in October.
- **Cybersecurity Reminder**: Please remember to use strong, unique passwords for all company systems and to report any suspicious emails or activities to our IT department.

**Cross-departmental Collaboration**

- **Joint Project**: We are collaborating with the Marketing department on a new customer retention campaign. More details will be shared in the coming weeks.
- **Cross-functional Learning**: We are offering shadowing opportunities with our Network Operations team. Interested employees should contact their supervisor.

**Health and Wellness**

- **Stress Management**: Remember to take regular breaks and practice stress-reducing techniques, such as deep breathing or meditation. Our Employee Assistance Program (EAP) offers resources and support.
- **Ergonomic Tips**: Ensure your workspace is set up to promote good posture and reduce eye strain. Our HR department can provide ergonomic assessments upon request.

**Fun and Engagement**

- **Employee Poll**: This month, we are asking: What do you think is the most important factor in providing excellent customer service? Share your thoughts with us!
- **Social Event**: Join us for our annual team-building event on October 29th. Details will be shared via email.

Thank you for your hard work and dedication to our customers. If you have any suggestions for future newsletter topics, please don't hesitate to reach out.


=============== 02-COPS Newsletter - October 2024.txt ===============

**Operational Updates**

- **Performance Metrics**: Our average customer satisfaction score for October was 93%, a 1% increase from September. Our average handling time (AHT) for customer calls was 4 minutes and 15 seconds, a 5% improvement.
- **Process Improvement**: We have identified an opportunity to streamline our order fulfillment process for new mobile contracts. A project team has been formed to implement these changes, with a target completion date of November 15th.

**Customer Insights**

- **Customer Feedback**: Customers have been praising our billing team for their clarity and patience when explaining charges and plans. One customer wrote, "The billing agent was very helpful and made sure I understood everything."
- **Common Issues**: We have seen an increase in inquiries about international roaming rates. To address this, we are updating our website FAQs and training our frontline staff to provide clearer information.

**Service Updates**

- **New Service Launch**: We are excited to announce the launch of our new fiber broadband plan, offering faster speeds and larger data allowances. Training on the new plan will be provided to all customer-facing staff.
- **Network Maintenance**: Our network operations team will be performing routine maintenance on our mobile network on October 25th, which may cause brief outages. We will notify affected customers in advance.

**Employee Spotlight**

- **Employee of the Month**: Congratulations to Michael Smith from our technical support team for his exceptional problem-solving skills and customer service. Michael consistently receives positive feedback from customers and colleagues.
- **Best Practices**: This month, we are highlighting the best practices of our customer retention team, who have implemented a new process for proactively contacting customers at risk of churn, resulting in a 20% reduction in cancellations.

**Training and Development**

- **Upcoming Training**: On October 20th, we will be offering a training session on advanced customer service skills, focusing on empathy and conflict resolution. All customer-facing staff are encouraged to attend.
- **Learning and Development**: Our L&D team has launched a new e-learning module on data protection and privacy. This module is available on our intranet and is mandatory for all employees.

**Industry News**

- **Regulatory Update**: The telecom regulator has announced new guidelines for customer complaint handling. We are reviewing these guidelines and will implement necessary changes to our processes.
- **Market Trends**: The latest market research shows an increase in demand for 5G services. We are well-positioned to meet this demand with our expanding 5G network.

**Technology Corner**

- **New Tool**: We are introducing a new chatbot tool to help manage customer inquiries more efficiently. Training on this tool will be provided in November.
- **Cybersecurity Reminder**: Please remember to use two-factor authentication for all company systems and to report any suspicious emails or activities to our IT department.

**Cross-departmental Collaboration**

- **Joint Project**: We are collaborating with the Sales department on a new customer acquisition campaign. More details will be shared in the coming weeks.
- **Cross-functional Learning**: We are offering shadowing opportunities with our IT department. Interested employees should contact their supervisor.

**Health and Wellness**

- **Mental Health Awareness**: October is Mental Health Awareness Month. Remember to prioritize your mental health and seek support if needed. Our EAP offers resources and counseling services.
- **Ergonomic Tips**: Ensure your workspace is set up to promote good posture and reduce eye strain. Our HR department can provide ergonomic assessments upon request.

**Fun and Engagement**

- **Employee Poll**: This month, we are asking: What do you think is the most challenging part of providing excellent customer service? Share your thoughts with us!
- **Halloween Celebration**: Join us for our annual Halloween celebration on October 31st. Details will be shared via email.

Thank you for your continued hard work and dedication to our customers. If you have any suggestions for future newsletter topics, please don't hesitate to reach out.


=============== 03-IT Newsletter - September 2024.txt ===============

Welcome to the September issue of TechConnect, your source for the latest updates from our IT department!

**Project Spotlight: 5G Network Expansion**

This month, we're excited to highlight our ongoing 5G network expansion project. Our team has successfully deployed 50 new 5G base stations across three major cities, significantly improving coverage and speed for our mobile customers. Special thanks to Sarah Chen and her network infrastructure team for their outstanding work!

**Key Achievements:**

- 30% increase in network capacity
- 40% reduction in latency
- 98.5% reliability rating in initial tests

**Innovation Corner: AI-Powered Customer Service**

Our AI and Machine Learning team has made significant strides in developing an advanced chatbot for customer service. Early tests show a 25% reduction in call center volume and a 15% increase in customer satisfaction scores. Great job to Alex Patel and the AI team!

**Cybersecurity Update**

**Attention all employees:** We've detected an increase in phishing attempts targeting telecom companies. Please be extra vigilant when opening emails, especially those requesting sensitive information. Remember:

1. Never share passwords via email
2. Double-check sender email addresses
3. Report suspicious emails to the security team

For more information, attend our upcoming "Cybersecurity Best Practices" webinar on September 15th.

**Data Analytics Insight**

Our data analytics team has uncovered an interesting trend: customers with bundled mobile and fiber services show 30% higher retention rates. This insight is now being used to inform our marketing and sales strategies.

**Sustainability Initiative**

We're proud to announce that our main data center has achieved a 15% reduction in energy consumption thanks to the implementation of advanced cooling systems and AI-driven resource allocation. Kudos to the infrastructure team for this achievement!

**New Team Members**

Please join us in welcoming our new team members:

- Maria Garcia - Senior Network Engineer
- Tom Wilson - Data Scientist
- Priya Sharma - UX Designer

**Learning & Development**

Don't miss out on these upcoming learning opportunities:

- "Introduction to Kubernetes" workshop - September 20th
- "Advanced Python for Data Analysis" online course - Starts October 1st

**Upcoming Events**

- IT Department Town Hall - September 25th
- Quarterly Hackathon - October 5-6th

**Employee Spotlight: Jack Thompson**

This month, we're featuring Jack Thompson from our Fiber-to-Home team. Jack's innovative approach to service activation has reduced installation times by 40%. Check out our blog for a full interview with Jack!

**Tech Tip of the Month**

Boost your productivity with this keyboard shortcut: Use Windows Key + V to access your clipboard history on Windows 10 and 11. This allows you to paste items you've copied previously!

That's all for this month's TechConnect! Remember, your feedback helps us improve.

Stay connected!

The IT Communications Team


===============04-IT Newsletter - October 2024.txt===============

Welcome to the October issue of TechConnect, your source for the latest updates from our IT department!

**Cybersecurity Month Special**

As October is Cybersecurity Awareness Month, we're dedicating a significant portion of this newsletter to security-related topics.

**New Telecom Cybersecurity Rules**

The Ministry of Communications has recently introduced the Telecommunications (Telecom Cyber Security) Rules, 2024. Key points include:

- Mandatory appointment of a Chief Telecommunication Security Officer (CTSO)
- Requirement to report security incidents within 6 hours
- Establishment of Security Operations Centers (SOC)

Our department is currently reviewing these rules to ensure full compliance. Stay tuned for updates on how this will affect our operations.

**AI-Powered Security Measures**

We're excited to announce the implementation of new AI-driven security algorithms to enhance our network protection. These measures will help us:

- Predict and prevent potential security breaches
- Optimize network performance
- Provide proactive maintenance solutions

**Project Spotlight: SASE Implementation**

This month, we're kicking off our Secure Access Service Edge (SASE) implementation project. SASE will help us:

- Integrate zero trust principles
- Enhance threat prevention
- Improve security for our remote workforce

**Innovation Corner: 6G Research**

Our R&D team has begun preliminary research into 6G technology. While 5G deployment is still ongoing, we're looking ahead to the next generation of mobile networks. This research will focus on:

- Ultra-high-speed connectivity
- Advanced AI integration
- Potential applications in augmented and virtual reality

**Data Analytics Insight**

Our data science team has developed a new predictive model for customer churn using machine learning techniques. Early results show a 15% improvement in churn prediction accuracy.

**Sustainability Update**

In line with our commitment to sustainability, we've achieved a 10% reduction in data center energy consumption this quarter through the implementation of AI-driven resource allocation.

**New Team Member Spotlight**

Please welcome our new Machine Learning Engineer, Dr. Sarah Chen. Sarah brings extensive experience in AI and will be leading our efforts in network optimization using machine learning.

**Learning & Development**

Don't miss these upcoming learning opportunities:

- "Introduction to SASE" webinar - October 15th
- "AI in Telecommunications" online course - Starts November 1st

**Upcoming Events**

- IT Department Town Hall - October 20th
- ENTELEC Conference & Expo - April 1-4, 2025 (Save the date!)

**Tech Tip of the Month**

Enhance your productivity with this AI-powered tool: Try using ChatGPT for brainstorming and problem-solving sessions. It can help generate ideas and provide different perspectives on complex issues.

That's all for this month's TechConnect! Remember, your feedback helps us improve.

Stay secure and connected!

The IT Communications Team


===============05-Networks Newsletter - September 2024.txt===============

**Technology Spotlight: Powering UltraFiber 2.0**

Our team has successfully implemented the network infrastructure to support the newly launched UltraFiber 2.0 service. Key technical achievements include:

- Deployment of XGS-PON technology enabling 10 Gbps symmetrical speeds
- Implementation of advanced traffic management algorithms to ensure ultra-low latency
- Integration of AI-driven security protocols for enhanced network protection

We're proud to provide the backbone for this groundbreaking service that's set to revolutionize residential internet experiences.

**Project Highlight: SmartCity Solutions Partnership**

Our 5G network expansion played a crucial role in the success of the SmartCity Solutions project. Network enhancements that facilitated this achievement include:

- Densification of small cells in urban areas to support IoT device connectivity
- Implementation of network slicing to prioritize critical city management traffic
- Deployment of edge computing nodes to reduce latency for real-time applications

These improvements not only supported SmartCity Solutions but will benefit all our 5G users in the area.

**Network Optimization: Supporting the "Triple Threat" Bundle**

To ensure seamless delivery of our new bundle offering, we've implemented several network optimizations:

- Enhanced interoperability between mobile and fixed-line networks for unified service delivery
- Upgraded core network capacity to handle increased data traffic from bundled services
- Implemented advanced QoS mechanisms to prioritize different service types within the bundle

These enhancements will ensure that customers experience consistent high-quality service across all bundled offerings.

**Capacity Planning: Back-to-School Bonanza**

In preparation for the upcoming Back-to-School promotion, we've taken the following steps to manage the expected surge in network usage:

- Increased backhaul capacity in areas with high student populations
- Optimized cell sites near educational institutions to handle higher data demands
- Implemented temporary "pop-up" small cells for added capacity during peak periods

These measures will ensure that both new and existing customers enjoy uninterrupted service during this high-traffic period.

**Technology Trends: eSIM Implementation Progress**

As eSIM technology gains traction, our team is working diligently to support this transition:

- Upgrading our Home Location Register (HLR) and Home Subscriber Server (HSS) to support eSIM profiles
- Implementing Over-the-Air (OTA) provisioning systems for seamless eSIM activation
- Conducting extensive testing to ensure compatibility with a wide range of eSIM-enabled devices

We're on track to fully support eSIM technology across our entire network by Q2 next year.

**Network Performance: Maintaining Our Competitive Edge**

Recent network enhancements have further improved our Silver Surfer plan's performance:

| Metric               | Previous Performance | Current Performance |
| -------------------- | -------------------- | ------------------- |
| Average Data Speed   | 15 Mbps              | 25 Mbps             |
| Call Setup Success   | 98.5%                | 99.3%               |
| Network Availability | 99.95%               | 99.98%              |

These improvements ensure that we continue to offer superior service quality compared to our competitors.

**Upcoming Initiatives**

- Beginning trials of 400G optical transport network to support future bandwidth demands
- Launching a pilot program for OpenRAN technology in select rural areas
- Initiating a network-wide energy efficiency audit to support our sustainability goals

Stay tuned for updates on these exciting projects in our next newsletter!

Your TeleCom Networks Team


===============06-Networks Newsletter - October 2024.txt===============

**Network Performance: UltraFiber 2.0 Rollout Success**

The successful launch of UltraFiber 2.0 is a testament to our network team's hard work:

- Achieved 99.99% uptime across all new installations
- Implemented dynamic bandwidth allocation, resulting in 400% average speed increase
- Optimized last-mile fiber connections, enabling 2-hour installation timeframes

Our network monitoring shows consistent 10 Gbps throughput, with latency under 2ms for most connections.

**Security Initiative: TeleCom Shield Infrastructure**

To support the new TeleCom Shield service, we've implemented several network-level enhancements:

- Deployed next-generation firewalls at network edges
- Integrated machine learning-based threat detection systems
- Established dedicated, high-capacity VPN servers in strategic locations
- Implemented advanced DNS filtering for parental controls

These improvements not only support TeleCom Shield but also enhance overall network security for all customers.

**Rural Connectivity Project: Greendale Success Story**

The Greendale project showcases our innovative approach to rural coverage:

- Utilized a combination of macro cells and small cells for optimal coverage
- Implemented TV White Space technology for long-range, obstacle-penetrating signals
- Deployed edge computing nodes to reduce latency for local services

These techniques will serve as a blueprint for future rural expansion projects.

**Network Capacity: Back-to-School Bonanza Impact**

Our proactive capacity planning paid off during the Back-to-School promotion:

- Peak data usage increased by 60%, handled without service degradation
- Successfully managed a 45% increase in simultaneous connections in college towns
- Dynamic spectrum sharing enabled seamless traffic management between 4G and 5G

**Technology Trend: Preparing for IoT Growth**

To support the growing IoT ecosystem, we're implementing several network upgrades:

- Deploying Narrow-Band IoT (NB-IoT) technology for low-power, wide-area coverage
- Enhancing network slicing capabilities to prioritize critical IoT traffic
- Increasing core network capacity to handle millions of additional connected devices

**Employee Wellness Integration: TeleCom Vitality**

We're supporting the new wellness program from a network perspective:

- Implementing secure data channels for fitness tracker synchronization
- Setting up dedicated servers for storing and analyzing employee health data
- Ensuring HIPAA compliance for all wellness program-related network traffic

**5G Network Enhancement**

In response to market competition, we're accelerating our 5G improvements:

- Achieved 85% urban area coverage, surpassing our initial targets
- Implemented Massive MIMO technology, boosting average speeds to 350 Mbps
- Began rural 5G trials using low-band spectrum for extended coverage
- Expanded mmWave deployment in high-density areas, offering speeds up to 2 Gbps

**Customer Loyalty Program: Technical Support**

To support the revamped TeleCom Rewards program, we've enhanced our network support capabilities:

- Implemented AI-driven predictive maintenance to prevent service interruptions for high-tier customers
- Established a dedicated network operations team for VIP support
- Developed a real-time network performance dashboard for customer service representatives

**Upcoming Projects**

- Initiating trials of 6G technologies in our research labs
- Planning the deployment of quantum-safe encryption across our core network
- Exploring satellite internet integration for ultra-remote areas

Stay connected and keep innovating!

Your TeleCom Networks Team


===============07-Sales Newsletter - September 2024.txt===============

**New Product Spotlight: UltraFiber 2.0**

We're thrilled to announce the launch of UltraFiber 2.0, our latest fiber-optic internet solution. This cutting-edge technology offers speeds up to 10 Gbps, making it the fastest residential internet service in the market. Key features include:

- Ultra-low latency for seamless gaming and video conferencing
- Advanced network security protocols
- Smart home integration capabilities

**Success Story: SmartCity Solutions**

Learn how our mobile services helped SmartCity Solutions revolutionize urban management. By leveraging our 5G network, they implemented IoT devices across the city, resulting in:

- 30% reduction in energy consumption
- 25% decrease in traffic congestion
- 40% improvement in waste management efficiency

**Sales Tip of the Month: Bundle and Save**

Boost your sales by promoting our new "Triple Threat" bundle. Customers can save up to 25% when combining mobile contracts, telephony services, and fiber cable. Remember to highlight the convenience of a single bill and unified customer support.

**Upcoming Promotion: Back-to-School Bonanza**

Get ready for our biggest back-to-school promotion yet! From September 15th to October 30th, we're offering:

- Free smartphone with any new 24-month mobile contract
- Double data allowance for students on all mobile plans
- $100 bill credit for new fiber cable installations

**Market Trends: The Rise of eSIM Technology**

Stay ahead of the curve by familiarizing yourself with eSIM technology. This emerging trend is set to revolutionize the mobile industry:

- 63% of smartphones will support eSIM by 2025
- Customers can easily switch between multiple profiles
- Reduces plastic waste from traditional SIM cards

**Top Performer Spotlight**

Congratulations to Sarah Johnson for achieving 150% of her sales target last month! Sarah attributes her success to:

1. Actively listening to customer needs
2. Tailoring solutions to specific use cases
3. Following up consistently with prospects

**Competitive Intelligence: Rival X's New Offering**

Rival X has launched a budget-friendly mobile plan targeting seniors. Here's how our Silver Surfer plan compares:

| Feature         | Our Silver Surfer Plan   | Rival X's Senior Plan    |
| --------------- | ------------------------ | ------------------------ |
| Monthly Cost    | $29.99                   | $34.99                   |
| Data Allowance  | 5GB                      | 3GB                      |
| Unlimited Calls | Yes                      | Yes                      |
| Family Discount | 15% off additional lines | 10% off additional lines |

Remember to emphasize our superior value and higher data allowance when discussing options with senior customers.

Stay connected and keep selling!

Your TeleCom Connect Team


===============08-Sales Newsletter - October 2024.txt===============

**Product Update: UltraFiber 2.0 Rollout Success**

Following last month's announcement, UltraFiber 2.0 has seen incredible adoption rates:

- 10,000+ new installations in the first month
- 98% customer satisfaction rating
- Average speed increase of 400% for upgrading customers

Our technicians report smoother installations than ever before, with most setups completed in under 2 hours.

**New Service Launch: TeleCom Shield**

Introducing TeleCom Shield, our comprehensive cybersecurity solution for both mobile and home internet:

- Real-time threat detection and blocking
- Virtual Private Network (VPN) for secure browsing
- Identity theft protection and dark web monitoring
- Parental controls and screen time management

**Success Story: Rural Connectivity Project**

Our mobile network expansion has transformed the farming community of Greendale:

- 95% coverage achieved across 500 square miles of rural terrain
- Local businesses report 40% increase in online sales
- Telemedicine services now available, reducing hospital visits by 25%

**Sales Strategy: Cross-Selling TeleCom Shield**

Boost your revenue by offering TeleCom Shield to existing customers:

1. Identify customers with multiple devices or children
2. Highlight the increasing cybersecurity threats in today's digital world
3. Offer a 30-day free trial with any service upgrade

**Promotional Update: Back-to-School Bonanza Results**

Our recent promotion was a massive success:

- 35% increase in new mobile contracts compared to last year
- 50% of new signups opted for the student double data plan
- Fiber cable installations up by 40% in college towns

**Market Insight: The Growth of IoT Devices**

The Internet of Things (IoT) is reshaping our industry:

- Global IoT connections expected to reach 25 billion by 2025
- Smart home devices sales increased by 30% last quarter
- Opportunity to upsell higher data plans for IoT-heavy households

**Employee Wellness Program**

We're excited to announce our new "TeleCom Vitality" program:

- Free fitness tracker for all employees
- Monthly step challenges with prizes
- Subsidized gym memberships
- Healthy snacks in all office locations

**Competitive Analysis: Rival Y's 5G Expansion**

Rival Y has accelerated their 5G rollout. Here's how we stack up:

| Feature         | Our 5G Network     | Rival Y's 5G Network |
| --------------- | ------------------ | -------------------- |
| Coverage        | 80% of urban areas | 75% of urban areas   |
| Average Speed   | 300 Mbps           | 250 Mbps             |
| Rural Expansion | Planned for Q4     | No announced plans   |
| mmWave Support  | Yes                | Limited              |

Emphasize our wider coverage and faster speeds when discussing 5G options with customers.

**Customer Retention Tip: Loyalty Program Relaunch**

Our revamped TeleCom Rewards program is now live:

- Points earned for every dollar spent on our services
- Exclusive early access to new products and features
- Tiered benefits including bill credits, device upgrades, and VIP support

Remember to inform existing customers about these new benefits to improve retention rates.

Stay innovative and keep connecting!

Your TeleCom Connect Team
				 """)
