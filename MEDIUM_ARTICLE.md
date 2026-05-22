# The PR as an Instruction Carrier: Beyond Simple CI/CD 🚀

In the world of DevOps, we often talk about "Continuous Delivery" as a pipeline that moves code from a developer's machine to a production server. But code is rarely a solitary traveler. It travels with companions: environment variables, database migrations, and infrastructure configurations.

When we ignore these companions, we get "Broken Deploys"—code that is perfect but fails because the environment wasn't ready.

This article introduces the philosophy of the **PR as an Instruction Carrier** and shows how to use **Business Rule Driven Design (BRDD)** to make your releases truly professional.

---

## ❌ The Problem: The "Context-Free" Merge
We've all seen it. A PR is approved, tests pass, and it's merged. Five minutes later, the site is down.
- **Why?** "Oh, I forgot to add the `STRIPE_API_KEY` to the production environment."
- **Why?** "I thought the migration was already run by the DBA."

The code was right, but the **instructions** for the deployment were lost in the noise.

## ✅ The Solution: The Instruction Carrier
A Pull Request should not just carry code; it must carry the **conditions** required for that code to function. If a PR requires a manual step, that step must be a **gate** that blocks the automated pipeline until it is satisfied.

---

## 🛠 Step-by-Step: Implementing Conditional Deployment Gates

Here is how we implemented this in the **Pyducts** project:

### 1. The PR Template (The Manual Contract)
We enforce a template in `.github/pull_request_template.md` that forces developers to declare their "Instruction Debt":

```markdown
### 🚧 Instruction Carrier (Deployment Gates)
Check the items that apply to this PR:
- [ ] **[DB_MIGRATION]**: This PR requires a database schema change.
- [ ] **[ENV_CHANGE]**: This PR requires new environment variables.
- [ ] **[BLOCK]**: Manual review required before release.
```

### 2. The Scanner (GitHub Action Gate)
We use a simple script in our CI pipeline to scan the PR body. If any of the markers are checked, the "Gate" job fails, preventing the "Production Promotion" from executing.

```yaml
# Simplified logic for the Deployment Gate
jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
      - name: Scan PR for Blockers
        run: |
          BODY=$(curl -s -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            ${{ github.event.pull_request.url }} | jq -r '.body')
          
          if echo "$BODY" | grep -q "\[x\] \*\*\[DB_MIGRATION\]\*\*"; then
            echo "❌ Database Migration Blocked!"
            exit 1
          fi
```

### 3. The Audit Trail (BRDD)
To make these instructions trustworthy, we use **Business Rule Driven Design (BRDD)**. By using the `brdd-python` library, every Use Case explicitly audits its side-effects:

```python
def execute(self, data) -> ExecutionContext:
    context = DefaultExecutionContext(data)
    # ... logic
    context.add_effect("EFF_NEW_TABLE_WRITE") # This justifies the DB_MIGRATION tag!
    return context
```

---

## 🎯 Conclusion: Moving to Professional Releases
When you treat your PR as an instruction carrier, you shift from "hoping it works" to "knowing it's ready." You empower your developers to take responsibility not just for the *logic*, but for the *behavior* of the system in production.

---
**Want to see the code?** Check out the [Pyducts Repository](https://github.com/leo-def/pyducts) for a live demonstration of these gates.
