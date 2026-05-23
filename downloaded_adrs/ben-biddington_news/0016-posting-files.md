# 16. posting files

Date: 2022-06-05

## Status

Accepted

## Context

See if we can post files without using `FormData.`

### How it works now

The `body` variable below is a `Buffer`. 

```ts
// src/adapters/web/fetch-based-internet.ts
private async postMultipart(url, headers, body) : Promise<Response> {
    this.log.info(`[FetchBasedInternet] Sending file to <${url}>`);
    this.log.info(`[FetchBasedInternet] Sending body <${JSON.stringify(body, null, 2)}>`);

    const formData = new FormData();

    formData.append("attachment", body);

    // [i] Let headers be auto-generated so that we get
    //
    //  multipart/form-data; boundary=--------------------------710326324172122735427581
    //

    //@ts-ignore
    const reply = await fetch(url, { headers: {}, method: 'post', body: formData }).
      then(async reply => ({ statusCode: reply.status, headers, body: (await reply.text()) }));

    return reply;
  }

```

Every time a file is attached whether by drag and drop or paste, it calls:

```ts
// src/adapters/application/real-diary-application.ts
await internet.post(
  `/diary/${attachment.diaryEntryId}/attachments`, 
  {
    'Content-type': 'multipart/form-data'
  }, 
  attachment.file
);
```


Which internally calls `postMultipart`.

`Attachment` looks like: 

```ts
// src/core/diary/attachment.ts
export class Attachment {
  id?: number;
  diaryEntryId: number;
  file: Buffer;
}
```

## Decision

The change that we're proposing or have agreed to implement.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.

## Notes

### Tests for file uploads

test/integration/web/api/diary/diary-api-examples.ts

This uses `postFile`:

```ts
// src/adapters/internet.js
// https://github.com/request/request#forms
const postFile = (url, headers, file) => {
  const request   = require("request");

  const formData = {
    attachments: [
      file
    ]
  }

  return new Promise(function(resolve, reject) {
    request.post({ url: url, formData: formData }, (error, reply, body) => {
      if (error){
        reject(error);
        return;
      }

      resolve(convertReply(reply, body));
    });  
  });
}
```

This is using the `request` library, which in turn uses the `form-data` package.

### Working with arrays in Javascript

In-browser, all of the API seem to be immutable.

But you [can do this](https://stackoverflow.com/questions/6965107/converting-between-strings-and-arraybuffers):

```js
var enc = new TextEncoder();
console.log(enc.encode("This is a string converted to a Uint8Array"));
```

### Comparing FormData with custom

Turns out string concatenation using backticks was somehow introducing tabs.

If you look at [the bad file](./assets/0016/001/unexpected-end) in VS Code it shows "Tab size: 2" in the bottom panel.

The [ok example](./assets/0016/001/ok) it reads "Spaces: 2".

After I changed it to use literal "\r\n" instead of multiline string with backticks it started working.

I also noticied in the network inspector the requests had different content length: no they are indentical.

