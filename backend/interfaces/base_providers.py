from abc import ABC, abstractmethod

class FinancialDataProvider(ABC):

    @abstractmethod
    def get_accounts(self):
        pass

    @abstractmethod
    def get_transactions(self, account_id):
        pass