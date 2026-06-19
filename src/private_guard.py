import argparse
import json
from dataclasses import dataclass

@dataclass
class PrivacySettings:
    ad_free: bool
    tracking_free: bool

class PrivateGuard:
    def __init__(self, settings: PrivacySettings):
        self.settings = settings

    def verify_ad_free(self) -> bool:
        return self.settings.ad_free

    def verify_tracking_free(self) -> bool:
        return self.settings.tracking_free

    def run(self) -> None:
        if not self.verify_ad_free():
            raise ValueError("Ad-free functionality not enabled")
        if not self.verify_tracking_free():
            raise ValueError("Tracking-free functionality not enabled")
        print("Private guard: ad-free and tracking-free functionality verified")

def main() -> None:
    parser = argparse.ArgumentParser(description="Private guard tool")
    parser.add_argument("--ad-free", action="store_true", help="Enable ad-free functionality")
    parser.add_argument("--tracking-free", action="store_true", help="Enable tracking-free functionality")
    args = parser.parse_args()

    settings = PrivacySettings(ad_free=args.ad_free, tracking_free=args.tracking_free)
    private_guard = PrivateGuard(settings)
    private_guard.run()

if __name__ == "__main__":
    main()
