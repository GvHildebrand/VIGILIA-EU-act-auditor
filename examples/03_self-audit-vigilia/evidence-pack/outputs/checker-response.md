# Free checker — how the generated snapshot is returned

The response body is generated text. The question for Article 50(2) is whether it
carries a machine-readable mark identifying it as artificially generated.

## Response construction

`vigilia/src/app/api/compliance/preview/route.ts`, final lines of the handler:

```ts
const response = Response.json(snapshot)
response.headers.set(
  'Set-Cookie',
  `${COOKIE_NAME}=${encodeRLCookie(newState)}; Path=/; Max-Age=…; SameSite=Lax; HttpOnly`
)
return response
```

## Payload shape

```ts
interface SnapshotResult {
  risk_tier: 'minimal' | 'limited' | 'high' | 'unacceptable'
  applicable_articles: string[]
  gap_count: number
  gap_types: string[]
  fine_exposure: string
  risk_reason: string      // generated prose, shown to the visitor
}
```

## What is absent

One header is set, and it is a rate-limiting cookie. There is **no provenance
header**, and no field in the payload marks `risk_reason` — the generated prose
the visitor reads — as artificially generated. Nothing that consumes this
response, including the visitor's own browser, can detect from the response that
its content is synthetic.
