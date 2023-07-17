#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  17 17:00:00 2023

@Author: Nicanor Kyamba
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Improves 12-log_stats.py by adding the top 10 of the most
    present IPs in the collection nginx of the database logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    """Total number of logs"""
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    """Methods count"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    """Status check count"""
    status_check_count = logs_collection.count_documents(
            {"method": "GET",
             "path": "/status"})
    print(f"{status_check_count} status check")

    """Top 10 IPs count"""
    top_ips = logs_collection.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
             }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
            }}
    ])
    print("IPs:")
    for ip in top_ips:
        ip = ip.get("ip")
        count = ip.get("count")
        print(f"\t{ip}: {count}")
