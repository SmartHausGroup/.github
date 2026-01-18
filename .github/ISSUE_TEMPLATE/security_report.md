---
name: Security Vulnerability Report
about: Report a security vulnerability
title: "[SECURITY] Brief description of the vulnerability"
labels: ["security", "vulnerability"]
assignees: []
---

## 🚨 Security Vulnerability Report

**IMPORTANT:** This issue template is for reporting security vulnerabilities only. For general security questions or discussions, please use our [security documentation](https://github.com/SmartHausGroup/.github/blob/main/SECURITY.md) or contact security@smarthaus.group.

---

## Vulnerability Details

**Summary**
Brief description of the security vulnerability.

**Severity**
- [ ] Critical - Immediate threat to production systems
- [ ] High - Significant security risk
- [ ] Medium - Moderate security concern
- [ ] Low - Minor security improvement needed

**Affected Components**
- Repository: [e.g., mge-core, TAI, RFS]
- Component: [e.g., API, SDK, Service]
- Versions affected: [e.g., v1.0.0 - v1.0.2]

**Attack Vector**
- Type: [e.g., Remote Code Execution, Data Breach, Denial of Service]
- Authentication required: [Yes/No]
- Privileges required: [e.g., None, User, Admin]

**Impact Assessment**
- Confidentiality impact: [None/Low/Medium/High]
- Integrity impact: [None/Low/Medium/High]
- Availability impact: [None/Low/Medium/High]
- User data exposure: [Yes/No]
- System compromise: [Yes/No]

## Technical Details

**Root Cause**
Technical explanation of the vulnerability:
- How it works
- Why it exists
- Code/system components involved

**Reproduction Steps**
Detailed steps to reproduce (DO NOT include exploits in public repos):

1. Step 1
2. Step 2
3. Expected vulnerable behavior

**Proof of Concept**
- [ ] POC code available (will share privately)
- [ ] POC code included above
- [ ] No POC available

## Mitigation

**Immediate Workaround**
Steps users can take to protect themselves:

**Permanent Fix**
Suggested solution approach:

**Patch Timeline**
- [ ] Patch available immediately
- [ ] Patch needed within 30 days
- [ ] Patch needed within 90 days
- [ ] No immediate patch needed

## Additional Information

**Related CVEs**
- CVE IDs: [if known]

**References**
- External references or research papers:

**Contact Information**
- Name: [Your name for acknowledgment]
- Preferred contact method: [email/chat]
- PGP Key: [if applicable]

---

## Confidentiality Notice

This vulnerability report will be treated with the highest confidentiality. We will:

1. Acknowledge receipt within 24 hours
2. Provide regular updates during investigation
3. Coordinate disclosure timing with you
4. Credit you in security advisories (if desired)
5. Follow responsible disclosure practices

Thank you for helping keep SMARTHAUS secure. Your contribution to our security is greatly appreciated.

---

**Submission Checklist:**
- [ ] I've provided clear technical details
- [ ] I've included reproduction steps
- [ ] I've assessed the severity level
- [ ] I've suggested mitigation approaches
- [ ] I'm available for follow-up questions

For urgent security issues requiring immediate attention, please email security@smarthaus.group directly.