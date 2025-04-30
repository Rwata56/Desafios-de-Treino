rotational_cipher <- function(text, key) {
  rotate_char <- function(char, key) {
    if (grepl("[a-z]", char)) {
      return(intToUtf8(((utf8ToInt(char) - utf8ToInt("a") + key) %% 26) + utf8ToInt("a")))
    } else if (grepl("[A-Z]", char)) {
      return(intToUtf8(((utf8ToInt(char) - utf8ToInt("A") + key) %% 26) + utf8ToInt("A")))
    }

    return(char)
  }

  chars <- unlist(strsplit(text, ""))
  rotated <- sapply(chars, rotate_char, key = key)
  return(paste(rotated, collapse = ""))
}

print(rotational_cipher("Attack at dawn!", 13))
print(rotational_cipher("Nggnpx ng qnja!", 13))
print(rotational_cipher("Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka?", 13))
print(rotational_cipher("Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka?", 26))
print(rotational_cipher("Kono Subarashii sekai ni shukufuku wo", 13))
print(rotational_cipher("Kono Subarashii sekai ni shukufuku wo", 0))
print(rotational_cipher(" ?", 13))
