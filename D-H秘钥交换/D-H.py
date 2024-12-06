import csv
import sympy
import pandas as pd

# 检查是否是原根
def is_primitive_root(prime, candidate):
    required_set = set(pow(candidate, power, prime) for power in range(1, prime))
    return len(required_set) == prime - 1

# 获取素数和原根
def find_primes_and_roots(start, end):
    primes = list(sympy.primerange(start, end + 1))
    data = []
    for prime in primes:
        for candidate in range(2, prime):
            if is_primitive_root(prime, candidate):
                data.append({"Prime": prime, "Primitive Root": candidate})
                break
    return data

# 按D-H协议计算共享密钥
def diffie_hellman(prime, root, private_key1, private_key2):
    # 公钥
    public_key1 = pow(root, private_key1, prime)
    public_key2 = pow(root, private_key2, prime)
    # 共享密钥
    shared_key1 = pow(public_key2, private_key1, prime)
    shared_key2 = pow(public_key1, private_key2, prime)
    assert shared_key1 == shared_key2  # 验证共享密钥一致性
    return public_key1, public_key2, shared_key1

# 主程序
def main():
    # 获取素数和原根
    prime_root_data = find_primes_and_roots(100, 255)

    # 构建输出表格
    results = []
    for item in prime_root_data:
        prime = item["Prime"]
        root = item["Primitive Root"]
        private_key1 = 6  # 用户A的私钥
        private_key2 = 15  # 用户B的私钥
        public_key1, public_key2, shared_key = diffie_hellman(prime, root, private_key1, private_key2)
        results.append({
            "Prime": prime,
            "Primitive Root": root,
            "Private Key A": private_key1,
            "Private Key B": private_key2,
            "Public Key A": public_key1,
            "Public Key B": public_key2,
            "Shared Key": shared_key
        })

    # 保存到CSV文件
    output_file = "dh_results.csv"
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"结果已保存到 {output_file}")

if __name__ == "__main__":
    main()
