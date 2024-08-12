const url = "https://movie.douban.com/cinema/nowplaying/suzhou/";
const isQuantumultX = typeof $task !== "undefined";
const isSurge = typeof $httpClient !== "undefined";
const isLoon = typeof $loon !== "undefined";

function getMovieData() {
  if (isQuantumultX) {
    $task.fetch({ url: url }).then(
      (response) =&gt; {
        showNotification(response.body);
      },
      (reason) =&gt; {
        console.log(reason.error);
        $done();
      }
    );
  } else if (isSurge || isLoon) {
    $httpClient.get(url, function (error, response, data) {
      if (error) {
        console.log(error);
        $done();
      } else {
        showNotification(data);
      }
    });
  }
}

function showNotification(data) {
  const movieData = extractMovieData(data);
  const movieTitles = movieData.titles.slice(0, 6);
  const movieScores = movieData.scores.slice(0, 6);
  const movieActors = movieData.actors.slice(0, 6);
  let notificationBody = "";
  for (let i = 0; i &lt; movieTitles.length; i++) {
    const score = movieScores[i] === "0" ? "æš‚æ— " : movieScores[i];
    const actors = movieActors[i] || "æš‚æ— ";
    notificationBody += "ðŸŽžï¸�" + movieTitles[i] + "-" + actors + "ðŸ�¿" + score + "\n";
  }

  if (isQuantumultX) {
    $notify("çƒ­æ˜ ç”µå½±&amp;è¯„åˆ†", "", notificationBody);
  } else if (isSurge || isLoon) {
    $notification.post("çƒ­æ˜ ç”µå½±&amp;è¯„åˆ†", "", notificationBody);
  }
  $done();
}

function extractMovieData(html) {
  const pattern = /data-title="(.*?)"\s+data-score="(.*?)"[^&gt;]+data-actors="(.*?)"/g;
  let matches;
  const titles = [];
  const scores = [];
  const actors = [];
  while ((matches = pattern.exec(html)) !== null) {
    const title = matches[1].trim();
    const score = matches[2].trim();
    const actorData = matches[3].trim();
    const actorList = actorData.split(" / ");
    titles.push(title);
    scores.push(score);
    actors.push(actorList);
  }
  return { titles: titles, scores: scores, actors: actors };
}

getMovieData();