export function removeEmptyKeys (dict) {
  for (const key in dict) {
    if (dict[key] === '') {
      delete dict[key]
    }
  }
  return dict
}
