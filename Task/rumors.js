const valueRegex = /<a !="undefined" !match[1])="" "请检查源码是否有${value}的值");="" $done();="" $httpclient="" $httpclient.get(sourceurl,="" $httpclient.get(targetcontenturl,="" $notification.post("获取${value}失败",="" $notification.post("获取谣言辟谣内容失败",="" $notification.post("获取辟谣内容失败",="" (!match="" (error)="" (error,="" (typeof="" )="" +="" ;="" const="" data)="" else="" error);="" function="" href="..\/(.*?)" if="" match="data.match(valueRegex);" response,="" rumorregex="/谣言：(.*?)&lt;\/strong" sourceurl="https://www.piyao.org.cn/jrpy/index.htm" targetcontenturl="targetUrl" targeturl="https://www.piyao.org.cn/" targetvalue="match[1];" targetvalue;="" useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36" {="" ||="" }="">&lt;\/span&gt;&lt;\/p&gt;/;
const truthRegex = /<strong>真相：&lt;\/strong&gt;(.*?)&lt;\/p&gt;/;
            const rumorMatch = data.match(rumorRegex);
            const truthMatch = data.match(truthRegex);

            if (!rumorMatch || !rumorMatch[1] || !truthMatch || !truthMatch[1]) {
              $notification.post("解析辟谣内容失败", "请检查辟谣内容的源码是否有变化");
            } else {
              const rumor = rumorMatch[1].replace(/&lt;[^&gt;]+&gt;/g, "").trim();
              const truth = truthMatch[1].replace(/&lt;[^&gt;]+&gt;/g, "").trim();
              const notificationContent = `今日谣言：${rumor}\n🔍真相：${truth}`;
              $notification.post("","",notificationContent);
            }
          }
          $done();
        });
      }
    }
  });
} else if (typeof $task !== "undefined") {
  $task.fetch({ url: sourceUrl }).then(
    function (response) {
      const data = response.body;
      const match = data.match(valueRegex);
      if (!match || !match[1]) {
        $notify("获取${value}失败", "请检查源码是否有${value}的值");
        $done();
      } else {
        const targetValue = match[1];
        const targetContentUrl = targetUrl + targetValue;

        $task.fetch({ url: targetContentUrl }).then(
          function (response) {
            const data = response.body;
            const rumorRegex = /<p tabindex="0">  <span style="color: .+?;"><strong>谣言：(.*?)&lt;\/strong&gt;&lt;\/span&gt;&lt;\/p&gt;/;
            const truthRegex = /<strong>真相：&lt;\/strong&gt;(.*?)&lt;\/p&gt;/;
            const rumorMatch = data.match(rumorRegex);
            const truthMatch = data.match(truthRegex);

            if (!rumorMatch || !rumorMatch[1] || !truthMatch || !truthMatch[1]) {
              $notify("解析辟谣内容失败", "请检查辟谣内容的源码是否有变化");
            } else {
              const rumor = rumorMatch[1].replace(/&lt;[^&gt;]+&gt;/g, "").trim();
              const truth = truthMatch[1].replace(/&lt;[^&gt;]+&gt;/g, "").trim();
              const notificationContent = `今日谣言：${rumor}\n🔍真相：${truth}`;
              $notify("","",notificationContent);
            }
            $done();
          },
          function (error) {
            $notify("获取辟谣内容失败", error);
            $done();
          }
        );
      }
    },
    function (error) {
      $notify("获取谣言辟谣内容失败", error);
      $done();
    }
  );
}
</strong></strong></span></p></strong></a>