from log_processor import load_logs, filter_logs
from analyzer import detect_suspicious_patterns, summarize_logs
from constants import ALERT_THRESHOLD

def main():
    logs = load_logs()
    print("=== AI Log Analyzer Tool v1 ===")
    print(f"Total logs loaded: {len(logs)}\n")
    
    summary = summarize_logs(logs)
    print(f"Summary: Total={summary['total']}, INFO={summary['info']}, WARN={summary['warnings']}, ERROR={summary['errors']}\n")
    
    suspicious = detect_suspicious_patterns(logs)
    if suspicious:
        print("⚠ Suspicious patterns detected:")
        for log, count in suspicious.items():
            print(f"{log} - {count} occurrences")
        if max(suspicious.values()) >= ALERT_THRESHOLD:
            print("\n!!! ALERT: Threshold exceeded !!!")
    else:
        print("No suspicious patterns detected.")
    
    keyword = input("\nEnter a keyword to filter logs (or press Enter to skip): ")
    if keyword:
        filtered = filter_logs(logs, keyword)
        print(f"Logs containing '{keyword}':")
        for log in filtered:
            print(log)

if __name__ == "__main__":
    main()
