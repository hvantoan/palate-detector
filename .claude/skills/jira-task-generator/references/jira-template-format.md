# Jira Template Format

## Required Sections

Every Jira task template MUST include all sections below. Use plain text formatting compatible with Jira's editor.

### TASK TITLE
- Clear, specific, action-oriented
- Bad: "Fix stuff", "Improve performance"
- Good: "Implement Redis Caching for Product Search API"

### SUMMARY
1-2 sentences describing the task objective. Answer: "What are we doing and why?"

### BACKGROUND / CONTEXT
- Why does this task exist?
- What problem does it solve?
- What triggered this work?
- Business impact or user pain point

### SCOPE OF WORK
Numbered or bulleted list of concrete implementation steps:
- Each step must be actionable by an engineer
- Include technical specifics: endpoints, models, configs
- Order steps logically (setup -> implement -> integrate -> verify)

### ACCEPTANCE CRITERIA
Checklist format using bullet points:
- Each criterion is independently verifiable
- Focus on observable behavior, not implementation details
- Include positive cases AND edge cases
- Use "Given/When/Then" format when appropriate

### DEFINITION OF DONE
Standard completion requirements:
- Code implemented and reviewed
- Unit/integration tests written and passing
- Documentation updated (if applicable)
- Deployed to staging and verified
- QA sign-off received
- Add project-specific requirements as needed

### DEPENDENCIES
- Related Jira tickets (blockers, related work)
- External systems or APIs
- Team dependencies (design, backend, DevOps)
- Environment requirements

### TECHNICAL NOTES (Optional)
- Architecture decisions or constraints
- Suggested approach or patterns
- Performance considerations
- Migration notes
- API contracts or data schemas

### TESTING NOTES
- What to test (happy path, edge cases, error scenarios)
- Test environments
- Test data requirements
- Regression concerns

### SUGGESTED LABELS
Comma-separated Jira labels. Common categories:
- Domain: `backend`, `frontend`, `devops`, `mobile`, `infra`
- Type: `feature`, `bugfix`, `tech-debt`, `security`, `performance`
- Priority hints: `critical`, `quick-win`, `spike`

## Formatting Rules

- Use plain text with bullet points (Jira-compatible)
- No markdown headers in output (use ALL CAPS section names)
- Keep sections concise — engineers scan, not read
- Infer missing details from context rather than asking
