<html><body><p>const url = "https://lishishangdejintian.bmcx.com/";
if (typeof $task !== "undefined") {
  $task.fetch({ url: url }).then(
    (response) =&gt; {
      const data = response.body.replace(/ /g, ' ');
      handleResponse(data);
    },
    (reason) =&gt; {
      console.log(reason.error);
      $done();
    }
  );
} else if (typeof $httpClient !== "undefined") {
  $httpClient.get(url, function (error, response, data) {
    if (error) {
      console.log(error);
      $done();
    } else {
      const sanitizedData = data.replace(/ /g, ' ');
      handleResponse(sanitizedData);
    }
  });
}

function handleResponse(data) {
  const regex = /(\d{4}年)(\d{1,2}月\d{1,2}日) <a href="\/\d+__lishishangdejintianchaxun\/" target="_blank">(.*?)&lt;\/a&gt;/g;
  const matches = [...data.matchAll(regex)];

  if (matches.length &gt; 0) {
    const today = new Date().getFullYear();
    const events = [];

    for (const match of matches) {
      events.push(`${match[1]} ${match[3]}`);
    }

    if (typeof $task !== "undefined") {
      $notify("历史上的今天", "", events.join("\n"));
    } else if (typeof $httpClient !== "undefined") {
      $notification.post("📓历史上的今天" ,"", events.join("\n"));
    }
  }

  $done();
}</a></p></body></html>