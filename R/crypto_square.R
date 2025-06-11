crypto_square <- function(text) {
  normalized <- tolower(gsub("[^a-zA-Z0-9]", "", text))
  n <- nchar(normalized)
  if (n == 0) return("")

  size <- ceiling(sqrt(n))
  padded <- paste0(normalized, strrep(" ", size^2 - n))

  matrix <- matrix(strsplit(padded, "")[[1]], nrow = size, byrow = TRUE)

  cols <- apply(matrix, 2, paste0, collapse = "")
  paste(trimws(cols), collapse = " ")
}

print(crypto_square("If man was meant to stay on the ground, god would have given us roots."))
print(crypto_square("Kono Subarashii sekai ni shukufuku wo"))
print(crypto_square("Dungeon ni Deai o Motomeru no wa Machigatteiru Darou ka?"))

