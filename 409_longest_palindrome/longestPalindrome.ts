function longestPalindrome(s: string): number {
  const map = {};
  let res = 0;

  for (let i of s) {
    if (i in map) {
      delete map[i];
      res++;
    } else {
      map[i] = 1;
    }
  }

  if (!isEmpty(map)) {
    return res * 2 + 1;
  }

  return res * 2;
}

function isEmpty(obj) {
  for (const prop in obj) {
    if (Object.hasOwn(obj, prop)) {
      return false;
    }
  }

  return true;
}
