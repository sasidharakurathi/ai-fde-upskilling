from datasets import load_dataset

ds = load_dataset("ucirvine/sms_spam", split="train")

print(ds)
print(ds[0])
print(ds.features)