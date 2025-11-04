``` markdown 
PythonProject1 - Mikhail Holmes Portfolio

A hybrid portfolio project demonstrating full-stack web development, cloud architecture design, and infrastructure-as-code principles.

## Table of Contents

- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Technology Stack](#technology-stack)
- [Detailed Project Structure](#detailed-project-structure)
- [Installation Guide](#installation-guide)
- [Usage & Features](#usage--features)
- [AWS Architecture Explained](#aws-architecture-explained)
- [Frontend Deep Dive](#frontend-deep-dive)
- [Python Diagram Generation](#python-diagram-generation)
- [Development Workflow](#development-workflow)
- [Deployment Strategy](#deployment-strategy)
- [Customization Guide](#customization-guide)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

PythonProject1 is a dual-purpose project that serves as both:

1. **A Professional Portfolio Website**: A clean, responsive, and interactive showcase of Mikhail Holmes' professional profile, resume, and projects
2. **A Cloud Architecture Documentation Tool**: Python-based automated generation of AWS infrastructure diagrams using the `diagrams` library

This project demonstrates:
- Modern web development practices
- Cloud architecture knowledge (AWS)
- Infrastructure-as-code (IaC) concepts
- Python scripting for documentation automation
- Professional software development workflows

### Why This Project Exists

The portfolio website provides a professional online presence while the Python diagram generator showcases technical skills in cloud architecture documentation. Together, they demonstrate both frontend and backend/DevOps capabilities to potential employers.

---

## Project Architecture

This project follows a hybrid architecture pattern:
```
┌─────────────────────────────────────────────────────────┐ │ PythonProject1 │ ├──────────────────────┬──────────────────────────────────┤ │ Web Frontend │ Python Backend/Tooling │ │ (Static HTML/CSS) │ (Diagram Generation) │ ├──────────────────────┴──────────────────────────────────┤ │ AWS Cloud Infrastructure │ │ (Amplify, CloudFront, Route 53, ACM) │ └─────────────────────────────────────────────────────────┘
``` 

**Key Design Principles:**
- **Separation of Concerns**: Frontend (HTML/CSS/JS) and tooling (Python) are clearly separated
- **Documentation as Code**: Infrastructure diagrams are generated programmatically
- **Static Site Optimization**: No server-side processing for fast, secure delivery
- **Cloud-Native**: Designed specifically for AWS Amplify deployment

---

## Technology Stack

### Frontend Technologies
| Technology | Purpose | Why It's Used |
|------------|---------|---------------|
| **HTML5** | Structure | Semantic markup for accessibility and SEO |
| **CSS3** | Styling | Modern CSS with custom properties (variables) for theming |
| **Vanilla JavaScript** | Interactivity | Lightweight, no framework overhead |

### Backend/Tooling Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.13.5 | Scripting and automation |
| **diagrams** | Latest | AWS architecture visualization |
| **virtualenv** | - | Isolated Python environment |

### Supporting Libraries
- **beautifulsoup4**: HTML/XML parsing (for potential web scraping)
- **requests**: HTTP library (for API calls if needed)
- **jinja2**: Template engine (for dynamic content generation)
- **pyyaml**: YAML configuration parsing
- **tornado**: Async networking library

### Cloud Infrastructure (AWS)
- **AWS Amplify**: Hosting and CI/CD
- **Amazon CloudFront**: CDN for global content delivery
- **Route 53**: DNS management
- **ACM (AWS Certificate Manager)**: SSL/TLS certificates

---

## Detailed Project Structure
```
PythonProject1/ │ ├── index.html # Main portfolio entry point │ └── Purpose: Landing page with navigation to all profile links │ ├── assets/ # Static frontend assets │ ├── style.css # Complete styling system │ │ ├── CSS custom properties for theming │ │ ├── Responsive design (@media queries) │ │ └── Modern effects (shadows, transitions, hover states) │ │ │ ├── app.js # JavaScript interactivity │ │ ├── Dynamic year footer │ │ ├── Button click handlers │ │ └── Navigation link management │ │ │ └── image/ # Image assets │ └── mikhail.jpg # Profile photo │ ├── docs/ # Generated documentation │ └── amplify_static_site_architecture.png │ └── Auto-generated AWS architecture diagram │ ├── script/ # Python automation scripts │ └── portfolio.py # AWS diagram generator │ ├── Defines AWS service nodes │ ├── Creates cluster hierarchies │ └── Generates visual architecture flows │ ├── .venv/ # Python virtual environment │ └── Isolated dependency management │ ├── .git/ # Version control │ └── Git repository for source control │ └── .idea/ # PyCharm IDE configuration └── Project-specific IDE settings
``` 

### File Responsibilities

#### `index.html`
- **Role**: Primary user interface
- **Features**:
  - Semantic HTML5 structure
  - Accessibility features (ARIA labels)
  - SEO-optimized meta tags
  - External link integration (Resume, LinkedIn, Medium, GitHub)
  - Interactive button for user engagement

#### `assets/style.css`
- **Role**: Visual presentation layer
- **Highlights**:
  - CSS Custom Properties (`--accent`, `--text`, `--card-bg`)
  - Mobile-first responsive design
  - Smooth transitions and animations
  - Card-based layout system
  - Professional color scheme

#### `assets/app.js`
- **Role**: Client-side interactivity
- **Functions**:
  - `DOMContentLoaded` event handler
  - Dynamic copyright year updates
  - Button click event management
  - Navigation link handling with external window opening

#### `script/portfolio.py`
- **Role**: Architecture documentation automation
- **Features**:
  - Uses `diagrams` library for AWS component visualization
  - Defines service relationships and data flows
  - Creates hierarchical cluster structures (Cloud → Region → VPC)
  - Exports to PNG format for documentation

---

## Installation Guide

### Prerequisites Checklist

Before starting, ensure you have:
- Python 3.13 or higher installed
- pip package manager
- virtualenv installed globally (`pip install virtualenv`)
- Git (for version control)
- PyCharm or any Python IDE (recommended)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Graphviz (required by diagrams library)

### Step 1: Clone the Repository
```
bash
# Clone from your repository
git clone [https://github.com/miholm10/PythonProject1.git](https://github.com/miholm10/PythonProject1.git)
# Navigate to project directory
cd PythonProject1
``` 

### Step 2: Set Up Python Environment
```
bash
# Activate the existing virtual environment
source .venv/bin/activate # macOS/Linux
# OR on Windows
.venv\Scripts\activate
# Verify Python version
python --version # Should show Python 3.13.5
``` 

### Step 3: Install Graphviz (Required for diagrams)

The `diagrams` library requires Graphviz for rendering:

**macOS:**
```
bash brew install graphviz
``` 

**Ubuntu/Debian:**
```
bash sudo apt-get install graphviz
``` 

**Windows:**
Download and install from [graphviz.org](https://graphviz.org/download/)

### Step 4: Install Python Dependencies
```
bash
# Install diagrams (main dependency for architecture visualization)
pip install diagrams
# Verify all packages are installed
pip list
``` 

You should see:
- beautifulsoup4
- diagrams
- graphviz
- requests
- jinja2
- pyyaml
- tornado

### Step 5: Verify Installation
```
bash
# Test the diagram generator
python script/portfolio.py
# Expected output: "docs generated successfully: amplify_static_site_architecture.png"
``` 

---

## Usage & Features

### Running the Portfolio Website

#### Option 1: Direct File Opening
```
bash
# Simply open in browser
open index.html # macOS start index.html # Windows xdg-open index.html # Linux
``` 

#### Option 2: Local Development Server
For a more production-like environment:
```
bash
# Python built-in server
python -m http.server 8000
# Then visit: [http://localhost:8000](http://localhost:8000)
``` 

#### Option 3: VS Code Live Server
If using VS Code, install the "Live Server" extension and click "Go Live"

### Portfolio Features Explained

#### 1. Profile Header
- Displays welcoming message
- Humorous, personality-driven copy
- Sets professional yet approachable tone

#### 2. Profile Photo
- Circular, bordered image
- Hover effect (slight scale up)
- Professional presentation
- Responsive sizing (adjusts on mobile)

#### 3. Navigation Links
Four primary call-to-action buttons:
- **Resume**: Google Drive link to downloadable PDF
- **LinkedIn**: Professional networking profile
- **Blog**: Medium articles demonstrating thought leadership
- **Projects**: GitHub repository showcase

**Technical Implementation:**
- Styled as button-like links for better UX
- `target="_blank"` for opening in new tabs
- Hover animations (color change, shadow, lift effect)

#### 4. Interactive Button
- Demonstrates JavaScript functionality
- Shows message on click
- Proves dynamic interactivity capability
- ARIA live region for accessibility

#### 5. Auto-Updating Footer
- JavaScript automatically updates copyright year
- No manual maintenance required
- Shows attention to detail

### Generating Architecture Diagrams
```
bash
# Generate the AWS Amplify architecture diagram
python script/portfolio.py
``` 

**What This Does:**
1. Imports AWS service node types from `diagrams` library
2. Creates a visual graph structure
3. Defines relationships between services (using `>>` operator)
4. Renders the diagram using Graphviz
5. Saves PNG image to project root or specified directory

**Diagram Components:**
- **User Node**: Represents local developer (PyCharm)
- **GitHub**: Version control repository
- **AWS Amplify**: Build and deployment service
- **CloudFront**: CDN for content distribution
- **Route 53**: DNS for custom domain
- **ACM**: SSL/TLS certificate management
- **End Users**: Global audience accessing the site

**Customization:**
```
python
# Change diagram direction
direction="LR" # Left to Right (current) direction="TB" # Top to Bottom direction="BT" # Bottom to Top direction="RL" # Right to Left
# Change output filename
filename="my_custom_architecture"
# Show diagram automatically (opens in default image viewer)
show=True # Automatically opens show=False # Saves only
``` 

---

## AWS Architecture Explained

### The Complete Flow
```
Developer (Local) ↓ (git push) GitHub Repository ↓ (webhook trigger) AWS Amplify (CI/CD) ↓ (build & deploy) Amazon CloudFront (CDN) ├→ Route 53 (DNS) ├→ ACM (HTTPS Cert) └→ End Users (Global)
``` 

### Service-by-Service Breakdown

#### 1. Local Development (PyCharm)
- **Role**: Development environment
- **Purpose**: Write code, test locally, commit changes
- **Integration**: Git push triggers deployment pipeline

#### 2. GitHub Repository
- **Role**: Version control and source of truth
- **Purpose**: Store code, track changes, trigger CI/CD
- **Amplify Integration**: Webhook listens for push events

#### 3. AWS Amplify
- **Role**: Hosting and CI/CD platform
- **Purpose**:
  - Automatically builds on git push
  - Runs build commands (if any)
  - Deploys to CloudFront
  - Provides preview URLs for branches
- **Configuration**: `amplify.yml` (not included, but would define build steps)
- **Benefits**:
  - Zero-config CI/CD
  - Automatic HTTPS
  - Branch previews
  - Atomic deployments

#### 4. Amazon CloudFront
- **Role**: Content Delivery Network (CDN)
- **Purpose**:
  - Caches content at edge locations worldwide
  - Reduces latency for global users
  - Handles SSL/TLS termination
  - Protects against DDoS
- **Benefits**:
  - Approximately 200+ edge locations globally
  - Automatic gzip compression
  - HTTP/2 support
  - Cost-effective bandwidth

#### 5. Route 53
- **Role**: DNS management
- **Purpose**:
  - Maps custom domain to CloudFront distribution
  - Provides fast DNS resolution
  - Health checks and failover (if needed)
- **Example Configuration**:
  ```
  mikhailholmes.com → CloudFront Distribution
  ```

#### 6. AWS Certificate Manager (ACM)
- **Role**: SSL/TLS certificate provider
- **Purpose**:
  - Free SSL certificates
  - Automatic renewal
  - Enables HTTPS for custom domain
- **Security**: Ensures encrypted connections (HTTPS)

### Cluster Hierarchy
```
AWS Cloud └── us-east-1 Region (required for CloudFront + ACM) └── VPC (Virtual Private Cloud) ├── AWS Amplify ├── CloudFront ├── Route 53 └── ACM
``` 

**Why us-east-1?**
- ACM certificates for CloudFront must be in us-east-1
- Industry standard for global services
- Lowest latency to most AWS services

### Security Considerations

1. **HTTPS Everywhere**: ACM provides free SSL certificates
2. **CloudFront Protection**: Built-in DDoS protection
3. **IAM Roles**: Amplify uses IAM for secure AWS access
4. **No Server Exposure**: Static hosting eliminates server vulnerabilities
5. **Content Security**: CloudFront can add security headers

### Cost Estimation

**Expected Costs (Monthly):**
- AWS Amplify: approximately $0.01-$0.15 (build minutes + hosting)
- CloudFront: approximately $0.10-$1.00 (based on traffic)
- Route 53: approximately $0.50 (hosted zone)
- ACM: **FREE**
- **Total**: approximately $0.60-$1.65/month for a personal portfolio

**AWS Free Tier Benefits:**
- Amplify: 1,000 build minutes/month
- CloudFront: 50GB data transfer out/month
- Route 53: 50M queries/month (not hosted zone)

---

## Frontend Deep Dive

### CSS Architecture

The stylesheet uses a **custom property system** for consistent theming:
```
css :root { --accent: #0073e6; /* Primary blue _/ --accent-dark: #005bb5; /_ Hover state _/ --text: #333; /_ Body text _/ --card-bg: #ffffff; /_ Card background _/ --page-bg: #f7f8fa; /_ Page background */ }
``` 

**Benefits:**
- Single source of truth for colors
- Easy theme switching
- Maintainable codebase
- CSS variable inheritance

### Responsive Design Strategy

The project uses a **mobile-first approach**:
```
css /* Base styles (mobile) */ .profile-img { width: 150px; height: 150px; }
/* Desktop enhancement */ @media (min-width: 521px) { .profile-img { width: 180px; height: 180px; } }
``` 

**Breakpoint Strategy:**
- Mobile: < 520px (stacked layout)
- Tablet/Desktop: > 520px (horizontal layout)

### CSS Features Used

1. **Flexbox**: For centering and layout
2. **CSS Grid**: (Could be added for more complex layouts)
3. **Transitions**: Smooth hover effects
4. **Box Shadow**: Depth and elevation
5. **Border Radius**: Modern rounded corners
6. **Transform**: Hover animations (scale, translateY)

### Accessibility Features

- **Semantic HTML**: `<header>`, `<main>`, `<footer>`, `<section>`
- **ARIA Labels**: `aria-live="polite"` for dynamic content
- **Alt Text**: All images have descriptive alt attributes
- **Focus States**: Keyboard navigation support
- **Color Contrast**: Meets WCAG AA standards

### Performance Optimizations

1. **Minimal Dependencies**: No external libraries (Bootstrap, jQuery, etc.)
2. **Inline Styles**: Critical CSS could be inlined for faster FCP
3. **Image Optimization**: Profile photo should be optimized/compressed
4. **Resource Hints**: Could add `<link rel="preconnect">` for external domains
5. **Font Loading**: Uses system fonts (no web font loading delay)

---

## Python Diagram Generation

### How the Diagrams Library Works

The `diagrams` library provides a **declarative, code-based approach** to creating architecture diagrams.

**Core Concepts:**

1. **Nodes**: Represent services/components
   ```python
   amplify = Amplify("AWS Amplify")
   ```

2. **Edges**: Represent connections/flows
   ```python
   github >> amplify  # Data flows from GitHub to Amplify
   ```

3. **Clusters**: Group related services
   ```python
   with Cluster("AWS Cloud"):
       # Services here are visually grouped
   ```

### Diagram Code Breakdown
```
python from diagrams import Cluster, Diagram
# Create diagram context
with Diagram( : # Define nodes developer = User("Local Development\n(PyCharm)") github = Github("GitHub Repository")
# Create hierarchical clusters
with Cluster("AWS Cloud"):
    aws_console = ManagementConsole("AWS Console")
    
    with Cluster("us-east-1 Region"):
        with Cluster("VPC"):
            amplify = Amplify("AWS Amplify\n(Build + Deploy)")
            cloudfront = CloudFront("Amazon CloudFront\n(CDN)")
            # ... more services

# Define data flows
developer >> github >> amplify
amplify >> cloudfront
cloudfront >> route53
latex_unknown_tag
``` 

### Advanced Customization

**Change Service Icons:**
```
python from diagrams.aws.compute import EC2 from diagrams.aws.database import RDS
ec2 = EC2("Web Server") db = RDS("Database") ec2 >> db # EC2 connects to RDS
``` 

**Multiple Outputs:**
```
python cloudfront >> [route53, acm] # CloudFront connects to both
``` 

**Bidirectional Flows:**
```
python from diagrams import Edge
app >> Edge(label="HTTPS") << cdn # Bidirectional with label
``` 

**Custom Colors:**
```
python with Diagram(..., graph_attr={"bgcolor": "transparent"}): # Transparent background
``` 

### Extending the Diagram

**Add More AWS Services:**
```
python from diagrams.aws.storage import S3 from diagrams.aws.security import IAM
s3 = S3("Asset Bucket") iam = IAM("Access Control")
amplify >> s3 # Amplify stores assets in S3 iam >> amplify # IAM controls Amplify access
``` 

**Add Monitoring:**
```
python from diagrams.aws.management import Cloudwatch
cw = Cloudwatch("Monitoring") cloudfront >> cw # CloudFront logs to CloudWatch
``` 

---

## Development Workflow

### Recommended Git Workflow
```
bash
# 1. Create feature branch
git checkout -b feature/add-contact-form
# 2. Make changes
# ... edit files ...
# 3. Test locally
python script/portfolio.py # Verify diagram generation open index.html # Test website
# 4. Stage and commit
git add . git commit -m "feat: add contact form with validation"
# 5. Push to GitHub
git push origin feature/add-contact-form
# 6. Create Pull Request
# ... on GitHub ...
# 7. Merge and deploy
# AWS Amplify automatically deploys on merge to main
``` 

### Commit Message Convention

Following **Conventional Commits**:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation only
- `style:` - Formatting, missing semicolons, etc.
- `refactor:` - Code restructuring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

Examples:
```
bash git commit -m "feat: add dark mode toggle" git commit -m "fix: resolve mobile nav overflow" git commit -m "docs: update README with deployment instructions"
``` 

### Local Testing Checklist

Before committing:
- [ ] HTML validates (use W3C validator)
- [ ] CSS has no errors (use CSS validator)
- [ ] JavaScript has no console errors
- [ ] Python script runs without errors
- [ ] All links work correctly
- [ ] Mobile responsive (test in DevTools)
- [ ] Images load properly
- [ ] Accessibility check (Lighthouse)

---

## Deployment Strategy

### AWS Amplify Setup

**Step 1: Connect Repository**
```
bash
# In AWS Console → Amplify
1. Click "New app" → "Host web app"
2. Select "GitHub"
3. Authorize AWS Amplify
4. Choose repository: PythonProject1
5. Select branch: main
``` 

**Step 2: Configure Build Settings**
```
yaml
# amplify.yml (create this file)
version: 1 frontend: phases: build: commands: - echo "Building static site..." artifacts: baseDirectory: / files: - '**/*' cache: paths: []
``` 

**Step 3: Set Up Custom Domain**
```
bash
# In Amplify Console → Domain management
1. Click "Add domain"
2. Enter your domain (e.g., mikhailholmes.com)
3. AWS automatically configures:
    - CloudFront distribution
    - ACM certificate
    - Route 53 DNS records

4. Wait for SSL certificate validation (~15 minutes)
``` 

### Deployment Pipeline
```
Git Push (main branch) ↓ AWS Amplify Webhook Triggered ↓ Provision: Set up build container ↓ Build: Run build commands (if any) ↓ Deploy: Upload to S3 + invalidate CloudFront ↓ Verify: Run tests (optional) ↓ Live: Site is now accessible
``` 

### Environment Variables

If you need configuration:
```
bash
# In Amplify Console → Environment variables
API_URL=[https://api.example.com](https://api.example.com) ENVIRONMENT=production
``` 

### Rollback Strategy
```
bash
# In Amplify Console
1. Click on deployment history
2. Select previous successful deployment
3. Click "Redeploy this version"

# Instantly rolls back to previous version
``` 

---

## Customization Guide

### Changing Colors (Theming)

Edit `assets/style.css`:
```
css :root { /* Dark theme example */ --accent: #00d9ff; --accent-dark: #00a8cc; --text: #e0e0e0; --card-bg: #1e1e1e; --page-bg: #121212; }
``` 

### Adding New Sections
```
html
Skills Python, JavaScript, HTML/CSS AWS (Amplify, CloudFront, Route 53) Git, CI/CD, DevOps
``` 

### Adding More Diagrams

Create new script:
```
python
# script/network_architecture.py
from diagrams import Diagram from diagrams.aws.network import VPC, ELB from diagrams.aws.compute import EC2
with Diagram("Network Architecture", show=False): vpc = VPC("VPC") lb = ELB("Load Balancer") web = EC2("Web Server")
vpc >> lb >> web
``` 

### Modifying Footer
```
javascript // In index.html
``` 

---

## Troubleshooting

### Common Issues & Solutions

#### Issue 1: "ImportError: cannot import name 'Region'"
**Cause**: The `diagrams` library doesn't have a `Region` class  
**Solution**: Remove the import and don't use `Region()` node
```
python
# Wrong
from diagrams.aws.general import Region region = Region("AWS Region")
# Correct
with Cluster("us-east-1 Region"): # Services here
``` 

#### Issue 2: Diagram not generating
**Cause**: Graphviz not installed  
**Solution**:
```
bash
# macOS
brew install graphviz
# Ubuntu
sudo apt-get install graphviz
# Windows
# Download from graphviz.org
``` 

#### Issue 3: CSS not loading
**Cause**: Incorrect file path  
**Solution**: Check path in `index.html`:
```
html
``` 

#### Issue 4: Virtual environment not activating
**Cause**: Wrong activation command  
**Solution**:
```
bash
# macOS/Linux
source .venv/bin/activate
# Windows (cmd)
.venv\Scripts\activate.bat
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
``` 

#### Issue 5: "Module not found" error
**Cause**: Package not installed in virtual environment  
**Solution**:
```
bash
# Ensure venv is activated (see prompt)
(.venv) $ pip install diagrams
# If still not working, recreate venv
deactivate rm -rf .venv python -m venv .venv source .venv/bin/activate pip install diagrams
``` 

### Debug Mode

Enable verbose Python output:
```
bash python -v script/portfolio.py
``` 

Check browser console:
```
Open DevTools (F12) → Console tab Look for JavaScript errors
``` 

---

## Contributing

While this is a personal portfolio project, improvements are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow existing code style
- Add comments for complex logic
- Test changes thoroughly
- Update README if needed
- Keep commits atomic and well-described

---

## License

© 2025 Mikhail Holmes. All rights reserved.

This project is for portfolio demonstration purposes. Feel free to use the structure and concepts, but please don't copy the personal content (name, photo, links).

---

## Author

**Mikhail Holmes**

- Email: mikhailholmes@yahoo.com
- LinkedIn: [linkedin.com/in/mikhailholmes](https://www.linkedin.com/in/mikhailholmes)
- GitHub: [github.com/miholm10](https://github.com/miholm10)
- Blog: [medium.com/@mikhailholmes2](https://medium.com/@mikhailholmes2)
- Resume: [View on Google Drive](https://drive.google.com/file/d/1ruJGhtlUhl2JRcMV5yiNT3XNONV58fcd/view)

---

## Acknowledgments

- **diagrams** library by mingrammer
- **AWS Amplify** team for excellent documentation
- **PyCharm** for the development environment
- The open-source community for inspiration

---

## Additional Resources

### Learning Resources
- [AWS Amplify Documentation](https://docs.amplify.aws/)
- [Diagrams Library Docs](https://diagrams.mingrammer.com/)
- [MDN Web Docs](https://developer.mozilla.org/) - HTML/CSS/JS reference
- [Python Official Docs](https://docs.python.org/3/)

### Related Projects
- [AWS Samples](https://github.com/aws-samples)
- [Static Site Generators](https://jamstack.org/generators/)

### Tools Used
- **IDE**: PyCharm 2024+
- **Version Control**: Git 2.x
- **Browser**: Chrome/Firefox with DevTools
- **Design**: Minimalist, professional aesthetic

---

## Future Enhancements

Potential improvements for v2.0:

- [ ] Add contact form with backend (AWS Lambda + API Gateway)
- [ ] Implement dark mode toggle
- [ ] Add blog section pulling from Medium RSS
- [ ] Create multiple architecture diagrams (compute, storage, etc.)
- [ ] Add animation library (AOS, GSAP)
- [ ] Implement i18n (internationalization)
- [ ] Add analytics (Google Analytics or AWS Pinpoint)
- [ ] Create PDF resume generator from YAML
- [ ] Add automated tests (pytest, Jest)
- [ ] Implement CI/CD with GitHub Actions

---

**Built with care by Mikhail Holmes | Last Updated: November 2025**
```
