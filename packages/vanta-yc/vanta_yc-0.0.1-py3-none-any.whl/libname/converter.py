import re
from datetime import datetime
import logging
import decimal
import pandas as pd

def convert_lob_log_table(logset_mdf_file_path):
    df = pd.DataFrame(columns=['Date_', 'Time', 'TimeStamp', 'idx', 'seqNum', 'symID', 'OrderbookID','vBid4', 'Bid4','vBid3', 'Bid3', 'vBid2', 'Bid2', 'vBid1', 'Bid1',\
                        'Ask1', 'vAsk1', 'Ask2', 'vAsk2', 'Ask3', 'vAsk3', 'Ask4', 'vAsk4'])
    rows_to_append = []
    with open(logset_mdf_file_path, 'r') as log_file:
        limitOrderbook_data = [] 
        counter = 0 
        lob_log_entry_pattern = re.compile(r'\[(.*?) (.*?)\] \[set_mdf_raw\] \[info\] limitOrderBook \[idx\],(\d+),\[sptId\],(\w+),\[prot\],(\w+),\[con\],(\d+),\[inv\],(\d+),\[seqNum\],(\d+),\[seconds\],(\d+),\[nanos\],(\d+),\[symId\],(\d+),\[.*?\],(\d+),\[b4\].*?,(.*?)\@(.*),\[b3\].*?,(.*?)\@(.*),\[b2\].*?,(.*?)\@(.*),\[b1\],(.*?)\@(.*)\,\|\|\,(.*?)\@(.*),\[a1],(.*?)\@(.*),\[a2],(.*?)\@(.*),\[a3],(.*?)\@(.*),\[a4]')
        for line in log_file:
            counter += 1
            match1 = lob_log_entry_pattern.match(line)
            if match1:
                Date = match1.group(1)
                Time = match1.group(2)
                Timestamp = str(match1.group(1)) + ' ' + str(match1.group(2))
                idx = int(match1.group(3))
                protocal = match1.group(4)
                con = str(match1.group(5))
                seqNum = int(match1.group(8))
                Second = int(match1.group(9))
                Nano = int(match1.group(10))
                symID = int(match1.group(11))
                OrderbookID = int(match1.group(12))
                vBid4 = int(match1.group(13))
                Bid4 = match1.group(14) 
                vBid3 = int(match1.group(15))
                Bid3 = match1.group(16)
                vBid2 = int(match1.group(17))
                Bid2 = match1.group(18)
                vBid1 = int(match1.group(19))
                Bid1 = match1.group(20)
                # print(f'Date: {Date}, Time: {Time}, Timestamp: {Timestamp}, idx: {idx}, seqNum: {seqNum}, Second: {Second}, Nano: {Nano}, symID: {symID}, OrderbookID: {OrderbookID}')
                # print(f'vBid4: {vBid4}, Bid4: {Bid4}, vBid3: {vBid3}, Bid3: {Bid3}, vBid2: {vBid2}, Bid2: {Bid2}, vBid1: {vBid1}, Bid1: {Bid1}')
                Ask1 = match1.group(21)
                vAsk1 = int(match1.group(22))
                Ask2 = match1.group(23)
                vAsk2 = int(match1.group(24))
                Ask3 = match1.group(25)
                vAsk3 = int(match1.group(26))
                Ask4 = match1.group(27)
                vAsk4 = int(match1.group(28))

                time_format = "%Y-%m-%d %H:%M:%S.%f"
                Timestamp = datetime.strptime(Timestamp, time_format)
                Timestamp = Timestamp.timestamp()
                limitOrderbook_data.append([Date, Time, Timestamp, idx, seqNum, Second, Nano, symID, OrderbookID, vBid4, Bid4, vBid3, Bid3, vBid2, Bid2, vBid1, Bid1, Ask1, vAsk1, Ask2, vAsk2, Ask3, vAsk3, Ask4, vAsk4])
                new_row = {'Date_': Date, 'Time': Time, 'TimeStamp': Timestamp, 'idx': idx, 'seqNum': seqNum, 'symID': symID, 'OrderbookID': OrderbookID,\
                        'vBid4': vBid4, 'Bid4': Bid4,'vBid3': vBid3, 'Bid3': Bid3, 'vBid2': vBid2, 'Bid2': Bid2, 'vBid1': vBid1, 'Bid1': Bid1,\
                        'Ask1': Ask1, 'vAsk1': vAsk1, 'Ask2': Ask2, 'vAsk2': vAsk2, 'Ask3': Ask3, 'vAsk3': vAsk3, 'Ask4': Ask4, 'vAsk4': vAsk4}
                rows_to_append.append(new_row)
                # df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True, sort=False)
    df = pd.concat([df, pd.DataFrame(rows_to_append)], ignore_index=True, sort=False)
    df['TimeStamp'] = pd.to_datetime(df['Date_'] + ' ' + df['Time'])
    cols = ['idx', 'seqNum', 'symID', 'OrderbookID','vBid4', 'Bid4','vBid3', 'Bid3', 'vBid2', 'Bid2', 'vBid1', 'Bid1',\
                        'Ask1', 'vAsk1', 'Ask2', 'vAsk2', 'Ask3', 'vAsk3', 'Ask4', 'vAsk4']
    df[cols] = df[cols].astype(float)
    columns = list(df.columns) 
    columns.insert(2, columns.pop(-1))
    return df[columns].sort_values(by = 'TimeStamp')

def convert_mbp_log_table(logset_mdf_file_path):
    rows_to_append = []
    df = pd.DataFrame()
    with open(logset_mdf_file_path, 'r') as log_file:
        # MarketByPrice_data = []
        counter = 0
        mbp_log_entry_pattern = re.compile(r'\[(.*?) (.*?)\] \[set_mdf_raw\] \[info\] MarketByPrice \[idx\],(\d+),\[.*?\],(\w+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\w+),\[.*?\],([-+]?\d+\.\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\w+),\[numDel\],(\d+),\[remain\],(\d+)')
        
        for line in log_file:
            counter += 1
            match2 = mbp_log_entry_pattern.match(line)
            if match2:
                Date = match2.group(1)
                Time = match2.group(2)
                Timestamp = match2.group(1) + ' ' + match2.group(2)
                idx = int(match2.group(3))
                protocal = match2.group(4)
                con = match2.group(5)
                seqNum = int(match2.group(6))
                Second = int(match2.group(7))
                Nano = int(match2.group(8))
                symID = int(match2.group(9))
                OrderbookID = int(match2.group(10))
                Side = match2.group(11)
                Price = decimal.Decimal(match2.group(12))
                Volume = int(match2.group(13))
                Level = int(match2.group(14))
                Action = match2.group(15)
                NumDel = int(match2.group(16))
                remain = int(match2.group(17))
                if remain >= 1:
                    remain =1
                time_format = "%Y-%m-%d %H:%M:%S.%f"
                Timestamp = datetime.strptime(Timestamp, time_format)
                Timestamp = Timestamp.timestamp()
                # MarketByPrice_data.append([Date, Time, idx, seqNum, Second, Nano, symID, OrderbookID, Side, Price, Volume, Level, Action, NumDel, protocal, con, remain])
                new_row = {'Date_': Date, 'Time': Time, 'idx': idx, 'seqNum': seqNum,'Second':Second, 'Nano': Nano, 'symID': symID, 'OrderbookID': OrderbookID, 'Side': Side, 'Price': Price, 'Volume': Volume, 'Level': Level,\
                            'Action': Action, 'NumDel': NumDel, 'protocal': protocal, 'con': con, 'remain': remain}
                rows_to_append.append(new_row)
        df = pd.concat([df, pd.DataFrame(rows_to_append)], ignore_index=True, sort=False)
        df['TimeStamp'] = pd.to_datetime(df['Date_'] + ' ' + df['Time'])
    cols = ['idx', 'seqNum', 'Second', 'Nano', 'symID',
        'OrderbookID', 'Side', 'Price', 'Volume', 'Level', 'NumDel',
        'protocal', 'con', 'remain']
    df[cols] = df[cols].astype(float)
    columns = list(df.columns) 
    columns.insert(2, columns.pop(-1))
    return df[columns].sort_values(by = 'TimeStamp') 

def convert_ttk_log_table(logset_mdf_file_path):
    rows_to_append = []
    df = pd.DataFrame()
    with open(logset_mdf_file_path, 'r') as log_file:
            TradeTickerMessage_data = []
            counter = 0
            ttk_log_entry_pattern = re.compile(r'\[(.*?) (.*?)\] \[set_mdf_raw\] \[info\] TradeTicker \[idx\],(\d+),\[.*?\],(\w+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(.*?),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+),\[.*?\],(\d+)')

            for line in log_file:
                counter += 1
                match3 = ttk_log_entry_pattern.match(line)
                if match3:
                    Date = match3.group(1)
                    Time = match3.group(2)
                    Timestamp = match3.group(1) + ' ' + match3.group(2)
                    idx = int(match3.group(3))
                    protocal = match3.group(4)
                    con = int(match3.group(5))
                    seqNum = int(match3.group(6))
                    Second = int(match3.group(7))
                    Nano = int(match3.group(8))
                    symID = int(match3.group(9))
                    OrderbookID = int(match3.group(10))
                    Price = decimal.Decimal(match3.group(11))
                    Volume = int(match3.group(12))
                    DealID = int(match3.group(13))
                    DealDateTime = int(match3.group(15))
                    Action = int(match3.group(16))
                    Agg = int(match3.group(17))
                    time_format = "%Y-%m-%d %H:%M:%S.%f"
                    Timestamp = datetime.strptime(Timestamp, time_format)
                    Timestamp = Timestamp.timestamp()
                    TradeTickerMessage_data.append([Date, Time, Timestamp, idx, seqNum, Second, Nano, symID, OrderbookID, Price, Volume, DealID, DealDateTime, Action, Agg, protocal, con])
                    new_row = {'Date_':Date, 'Time': Time, 'idx': idx, 'seqNum': seqNum, 'Second':Second, 'Nano':Nano, 'symID':symID,\
                            'OrderbookID': OrderbookID, 'Price': Price, 'Volume': Volume, 'DealID': DealID, 'DealDateTime': DealDateTime, 'Action': Action, 'Agg': Agg, 'protocal': protocal, 'con': con}
                    rows_to_append.append(new_row)
            df = pd.concat([df, pd.DataFrame(rows_to_append)], ignore_index=True, sort=False)
            df['TimeStamp'] = pd.to_datetime(df['Date_'] + ' ' + df['Time'])
            cols = ['idx', 'seqNum', 'Second', 'Nano', 'symID','OrderbookID', 'Price', 'Volume', 'DealID', 'DealDateTime', 'Agg', 'protocal', 'con']
            df[cols] = df[cols].astype(float)
            columns = list(df.columns) 
            columns.insert(2, columns.pop(-1))
            return df[columns].sort_values(by = 'TimeStamp')
    

# if __name__ == "__main__": 
#     logset_mdf_file_path = '/media/yatipa_drive/DW_SET50/dataset/extract_log_file/set_mdf_raw_2024-02-27.log'
#     df = convert_ttk_log_table(logset_mdf_file_path)
#     print(df)