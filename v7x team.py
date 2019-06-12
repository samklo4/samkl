import hashlib
text =str(input("Enter text :"))
hash_type = str(input("Entet Hash typr : "))
text = text.encode('utf-8')
hash_hash = hashlib.new(hash_type)
hash_hash.update(text)
hasher = hash_hash.hexdigest()
print (hasher)