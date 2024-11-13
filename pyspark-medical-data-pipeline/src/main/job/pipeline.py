from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, lit, col

class PySparkJob:
    def __init__(self):
        """Initialize a Spark session for processing medical and eligibility data"""
        self.spark = SparkSession.builder \
            .appName("Medical Data Processing") \
            .getOrCreate()

    def read_csv(self, path, schema):
        """
        Read CSV file into a Spark DataFrame with the specified schema
        
        Args:
            path: String path to the CSV file
            schema: StructType schema defining the DataFrame structure
            
        Returns:
            DataFrame containing the CSV data
        """
        return self.spark.read.csv(path, header=True, schema=schema)

    def filter_medical(self, eligibility, medicals):
        """
        Filter medical records to only include members present in eligibility
        
        Args:
            eligibility: DataFrame with eligibility records
            medicals: DataFrame with medical records
            
        Returns:
            DataFrame with filtered medical records
        """
        # Just return medical records that have matching memberIds in eligibility
        return medicals.join(
            eligibility.select("memberId"), 
            ["memberId"], 
            "inner"
        )

    def generate_full_name(self, eligibility, filtered_medical):
        """
        Generate full names for medical records by combining first and last names
        
        Args:
            eligibility: DataFrame with eligibility records
            filtered_medical: DataFrame with filtered medical records
            
        Returns:
            DataFrame with medical records including full names
        """
        # Create full name by concatenating first and last names
        result = filtered_medical.join(
            eligibility,
            ["memberId"],
            "inner"
        ).withColumn(
            "fullName",
            concat(col("firstName"), lit(" "), col("lastName"))
        )
        
        # Select only the required columns to match the medical schema
        return result.select("memberId", "fullName", "paidAmount")

    def find_max_paid_member(self, medicals):
        """
        Find the member ID with the highest paid amount
        
        Args:
            medicals: DataFrame with medical records
            
        Returns:
            String containing the member ID with highest paid amount
        """
        # Order by paidAmount descending and take the first record
        max_paid = medicals.orderBy(col("paidAmount").desc()).first()
        return max_paid.memberId if max_paid else None

    def find_total_paid_amount(self, medicals):
        """
        Calculate the total paid amount across all medical records
        
        Args:
            medicals: DataFrame with medical records
            
        Returns:
            Integer representing the total paid amount
        """
        result = medicals.agg({"paidAmount": "sum"}).first()
        return result[0] if result else 0

    def stop(self):
        """Stop the Spark session"""
        self.spark.stop()
