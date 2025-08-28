"""
# CityLink Farebox (Python Version)
====================================

## Overview
CityLink Farebox is a Python application that computes metro ride charges by inferring fare rules from tap log data. 
The initial rules (Base Fare, Peak Period Surcharge, Transfer Window, Night Discount, and Post-Midnight Discount) 
are implemented as separate, toggleable classes. Each rule processes a tap event and updates the fare accordingly.

## Fare Rules Hypothesis
The following rules are applied:
1. **BaseFareRule:** Sets a base fare of ₹25.
2. **PeakPeriodRule:** Applies an extra surcharge during peak periods (8–10 AM and 6–8 PM).
3. **TransferWindowRule:** Represents a placeholder for free transfers within a 30-minute window.
4. **NightDiscountRule:** Applies a 20% discount on fares between 10 AM and midnight.
5. **PostMidnightRule:** Applies a 35% discount on fares from midnight to 4 AM.

Each rule is implemented as an independent, toggleable class, allowing for rapid A/B testing of combined fare scenarios.

## Class Design
- **TapRecord:** Encapsulates details of a tap, including datetime, metro line, station, and charged fare.
- **FareRule (Base Class):** Defines a common interface (`apply`) for all fare rules.
- **Concrete Fare Rules:**  
  - BaseFareRule, PeakPeriodRule, TransferWindowRule, NightDiscountRule, PostMidnightRule.
- **TariffEngine:** Chains the enabled rules to compute the fare for each tap log entry.
- **Main Application:** Reads sample tap records, computes fares via TariffEngine, and prints the results.

## How to Execute
### Requirements
- Python 3.6 or higher.

### Run the Application
1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Execute the following command:
        
        python CityLinkFarebox.py

This will process sample tap records and print the computed fare for each.

------------------------------------
Deliverables Embedded:
1. Hypothesis Brief – Describes each rule from R1 to R5, making each testable.
2. Class Design Note – Explains the responsibilities of TapRecord, FareRule (and its concrete implementations) and TariffEngine.
3. Code Implementation – Implements the rules as independent, toggleable classes.
4. Switch Tests On/Off – Each rule can be toggled via a Boolean flag when instantiated in main().

------------------------------------
Fare Rules Implemented:
- BaseFareRule: R1 - Sets a base fare of ₹25.
- PeakPeriodRule: R2 - Adds a surcharge of ₹10 during peak hours (08:00–10:00 or 18:00–20:00).
- TransferWindowRule: R3 - Placeholder for the free transfer window (within 30 minutes).
- NightDiscountRule: R4 - Applies a 20% discount for rides between 10:00 and midnight.
- PostMidnightRule: R5 - Applies a 35% discount for rides between midnight and 04:00.

TariffEngine processes each tap record by applying the enabled rules in sequence.
"""

from datetime import datetime, timedelta

class TapRecord:
    """
    Represents a single entry from the tap log.

    Attributes:
        datetime_str (str): String representation of the tap's datetime (e.g., "07-01 07:20").
        line (str): Metro line identifier.
        station (str): Station code.
        charged_amount (float): The fare that was charged (from the anonymized tap log).
        datetime (datetime): Parsed datetime object from datetime_str.
    """
    def __init__(self, datetime_str, line, station, charged_amount):
        self.datetime_str = datetime_str
        self.line = line
        self.station = station
        self.charged_amount = charged_amount
        self.datetime = datetime.strptime(datetime_str, "%m-%d %H:%M")
        
    def __str__(self):
        return f"{self.datetime_str} | Line: {self.line} | Station: {self.station} | Charged: {self.charged_amount}"

class FareRule:
    """
    Base class for all fare rules.

    Attributes:
        active (bool): Flag to indicate if a rule is enabled.
    """
    def __init__(self, active=True):
        self.active = active
        
    def apply(self, tap_record, current_fare):
        """
        Applies the rule to the tap record.

        Parameters:
            tap_record (TapRecord): The tap record to process.
            current_fare (float): The fare computed from previous rules.
            
        Returns:
            float: The updated fare after applying this rule.
        """
        return current_fare

class BaseFareRule(FareRule):
    """
    R1 - BaseFareRule:
    Sets a base fare of ₹25 irrespective of other conditions.
    """
    def apply(self, tap_record, current_fare):
        if not self.active:
            return current_fare
        return 25

class PeakPeriodRule(FareRule):
    """
    R2 - PeakPeriodRule:
    Adds a surcharge during peak hours.
    
    Peak Hours:
        - 08:00 to 10:00 (morning peak)
        - 18:00 to 20:00 (evening peak)
    
    Surcharge:
        +₹10 applied during these periods.
    """
    def apply(self, tap_record, current_fare):
        if not self.active:
            return current_fare
        dt = tap_record.datetime
        if (dt.hour >= 8 and dt.hour < 10) or (dt.hour >= 18 and dt.hour < 20):
            return current_fare + 10
        return current_fare

class TransferWindowRule(FareRule):
    """
    R3 - TransferWindowRule:
    Implements the transfer window logic.
    
    If a tap occurs within 30 minutes of the last tap, it would be considered a free transfer.
    Currently, this is a placeholder since a full implementation requires tracking previous taps.
    """
    def apply(self, tap_record, current_fare):
        if not self.active:
            return current_fare
        # Placeholder for transfer window logic.
        return current_fare

class NightDiscountRule(FareRule):
    """
    R4 - NightDiscountRule:
    Applies a 20% discount on the fare for rides between 10:00 and midnight.
    """
    def apply(self, tap_record, current_fare):
        if not self.active:
            return current_fare
        dt = tap_record.datetime
        if 10 <= dt.hour < 24:
            return current_fare * 0.8
        return current_fare

class PostMidnightRule(FareRule):
    """
    R5 - PostMidnightRule:
    Applies a 35% discount on the fare for rides between midnight and 04:00.
    """
    def apply(self, tap_record, current_fare):
        if not self.active:
            return current_fare
        dt = tap_record.datetime
        if 0 <= dt.hour < 4:
            return current_fare * 0.65
        return current_fare

class TariffEngine:
    """
    Computes the fare for a tap record by applying a series of fare rules.

    Attributes:
        rules (list): A list of fare rule instances to process.
    """
    def __init__(self, rules):
        self.rules = rules
        
    def compute_fare(self, tap_record):
        """
        Applies each active fare rule sequentially.

        Parameters:
            tap_record (TapRecord): The tap event record.
            
        Returns:
            float: The final computed fare.
        """
        fare = 0
        for rule in self.rules:
            fare = rule.apply(tap_record, fare)
        return fare

def main():
    """
    Main execution function.
    
    Initializes sample tap log records, configures the active fare rules,
    computes the fare for each tap using TariffEngine, and prints the results.
    """
    # Sample tap log records
    taps = [
        TapRecord("07-01 07:20", "G", "BD", 25),
        TapRecord("07-01 08:01", "G", "NC", 37.5),
        TapRecord("07-01 08:30", "R", "YH", 0),
        TapRecord("07-01 10:01", "R", "KL", 25),
        TapRecord("07-01 14:36", "G", "NC", 25),
        TapRecord("07-01 22:15", "Y", "BD", 20),
        TapRecord("07-03 00:20", "R", "NC", 16.25)
    ]
    
    # Configure the active fare rules (toggle each "active" flag as needed for testing)
    rules = [
        BaseFareRule(active=True),
        PeakPeriodRule(active=True),
        TransferWindowRule(active=True),
        NightDiscountRule(active=True),
        PostMidnightRule(active=True)
    ]
    
    # Create TariffEngine with specified rules
    engine = TariffEngine(rules)
    
    # Process each tap record and output the computed fare
    for tap in taps:
        computed = engine.compute_fare(tap)
        print(f"Record: {tap} => Computed Fare: {computed}")
    
if __name__ == "__main__":
    main()