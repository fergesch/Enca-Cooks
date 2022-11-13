import Api from "../utils/Api.vue";

export function fiveLetter(word) {
  //makes copy of word, removes whitespace and changes case, checks length and if all letters
  let abc = word.slice();
  abc = abc.trim().toLowerCase();
  if (abc.length == 5 && !/[^a-z]/i.test(abc)) {
    return abc;
  } else {
    // console.log(abc)
    return false;
    //display error
  }
}

export function toggleMatch(x) {
  if (x == -1) {
    return 0;
  } else if (x == 0) {
    return 1;
  } else if (x == 1) {
    return -1;
  }
}

export async function checkWord(abc) {
  const wordClean = fiveLetter(abc.slice());
  if (wordClean) {
    const resp = await Api.get("/checkWord", { params: { word: wordClean } });
    return resp["data"];
  } else {
    // console.log(false)
    return false;
  }
}
