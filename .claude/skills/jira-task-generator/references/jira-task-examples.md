# Jira Task Examples

## Example 1: Backend Feature

Input: "Create login error handling"

TASK TITLE
Improve Login Error Handling

SUMMARY
Implement improved error messages and validation during login attempts.

BACKGROUND / CONTEXT
Users currently receive generic login errors, which reduces usability and support efficiency. Clear error messaging will reduce support tickets and improve user experience.

SCOPE OF WORK
- Implement validation for empty fields (email, password)
- Add incorrect password error messaging with remaining attempts
- Handle locked account responses (show unlock instructions)
- Ensure error messages are localized (i18n support)
- Return structured error codes from backend API

ACCEPTANCE CRITERIA
- Users see specific error messages for each failure type
- API returns appropriate HTTP status codes (400, 401, 403, 429)
- Error messages appear inline under the relevant input field
- Locked accounts show unlock/reset instructions
- Empty field validation triggers before API call

DEFINITION OF DONE
- Feature implemented and code reviewed
- Unit tests added for all error scenarios
- QA verified behavior on staging
- Localization strings added for supported languages

DEPENDENCIES
- Authentication API (error code contract)
- UI login component (error display slots)
- i18n service (translation keys)

TECHNICAL NOTES
Ensure backend returns structured error response: { code, message, details }. Frontend maps error codes to localized strings.

TESTING NOTES
Test: incorrect credentials, locked accounts, empty inputs, rate limiting (429), network errors. Verify error messages clear on retry.

SUGGESTED LABELS
authentication, ux, login, frontend, backend

---

## Example 2: Performance Optimization

Input: "Add caching to product search"

TASK TITLE
Implement Caching for Product Search API

SUMMARY
Improve search performance by caching frequent product queries using Redis.

BACKGROUND / CONTEXT
Current product search queries hit the database directly, causing high load during peak traffic (Black Friday saw 3x latency). Caching will reduce DB pressure and improve response times.

SCOPE OF WORK
- Introduce Redis caching layer for search service
- Cache top 1000 most frequent queries with TTL
- Implement cache invalidation on product create/update/delete
- Add cache-hit/miss metrics to monitoring dashboard
- Configure Redis connection pooling

ACCEPTANCE CRITERIA
- Repeated search queries served from cache (< 50ms)
- Cache invalidated within 5s of product changes
- Search latency improves by >= 30% on cached queries
- Cache metrics visible in monitoring dashboard
- Graceful degradation when Redis is unavailable

DEFINITION OF DONE
- Redis integration complete and reviewed
- Cache invalidation tested with product CRUD operations
- Monitoring dashboard updated with cache metrics
- Performance benchmarks documented
- Deployed to staging, load tested

DEPENDENCIES
- Redis instance (provisioned by DevOps)
- Search service (integration point)
- Product service (invalidation webhooks)
- Monitoring stack (Grafana/Datadog)

TECHNICAL NOTES
Key format: `search:{normalized_query_hash}`. TTL: 15 minutes. Use write-through invalidation pattern. Normalize queries before hashing (lowercase, sort params).

TESTING NOTES
Validate: cache hit/miss behavior, TTL expiration, invalidation on product update, Redis failover (fallback to DB), concurrent cache writes.

SUGGESTED LABELS
performance, backend, caching, redis

---

## Example 3: Bug Fix

Input: "Users can't upload images larger than 2MB"

TASK TITLE
Fix Image Upload Size Limit Blocking Files Over 2MB

SUMMARY
Increase image upload limit from 2MB to 10MB and add proper error messaging for oversized files.

BACKGROUND / CONTEXT
Users report inability to upload profile photos and product images larger than 2MB. The current limit is set at the nginx proxy level without corresponding frontend validation, causing silent failures.

SCOPE OF WORK
- Update nginx client_max_body_size to 10MB
- Update API file upload middleware limit to 10MB
- Add frontend file size validation before upload (show error for > 10MB)
- Add image compression option for files between 5-10MB
- Update error responses to include max size info

ACCEPTANCE CRITERIA
- Images up to 10MB upload successfully
- Files > 10MB show clear error with size limit info
- Frontend validates file size before sending request
- Upload progress indicator works for larger files
- Existing images unaffected by change

DEFINITION OF DONE
- Nginx and API configs updated
- Frontend validation added with error messaging
- Tested with files at boundary sizes (2MB, 5MB, 10MB, 11MB)
- Deployed to staging and verified

DEPENDENCIES
- Nginx configuration (DevOps access)
- File upload API middleware
- Frontend upload component
- Storage service (verify capacity)

TECHNICAL NOTES
Check all proxy layers (nginx, API gateway, load balancer) for body size limits. Update in order: storage -> API -> proxy -> frontend.

TESTING NOTES
Test with: 1MB (pass), 5MB (pass), 10MB (pass), 10.1MB (fail with message), various image formats (JPEG, PNG, WebP). Test on slow connections for timeout handling.

SUGGESTED LABELS
bugfix, upload, frontend, backend, infrastructure
