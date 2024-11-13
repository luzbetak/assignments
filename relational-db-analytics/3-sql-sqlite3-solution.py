#!/usr/bin/env python

import sqlite3

DB_PATH = "sandbox.db"  # SQLite database file path

def load_data():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS unlabeled_image_predictions (
        image_id INTEGER PRIMARY KEY,
        score REAL
    );
    """

    insert_data_query = """
    INSERT OR IGNORE INTO unlabeled_image_predictions (image_id, score) VALUES
    (828,  0.3149),  (705,  0.9892),  (46,   0.5616),  (594,  0.7670),
    (232,  0.1598),  (524,  0.9876),  (306,  0.6487),  (132,  0.8823),
    (906,  0.8394),  (272,  0.9778),  (616,  0.1003),  (161,  0.7113),
    (715,  0.8921),  (109,  0.1151),  (424,  0.7790),  (609,  0.5241),
    (63,   0.2552),  (276,  0.2672),  (701,  0.0758),  (554,  0.4418),
    (998,  0.0379),  (809,  0.1058),  (219,  0.7143),  (402,  0.7655),
    (363,  0.2661),  (624,  0.8270),  (913,  0.2421),  (439,  0.3387),
    (464,  0.3674),  (405,  0.6929),  (986,  0.8931),  (344,  0.3761),
    (847,  0.4889),  (482,  0.5023),  (823,  0.3361),  (617,  0.0218),
    (47,   0.0072),  (867,  0.4050),  (96,   0.4498),  (126,  0.3564),
    (943,  0.0452),  (115,  0.5309),  (417,  0.7168),  (706,  0.9649),
    (166,  0.2507),  (991,  0.4191),  (465,  0.0895),  (53,   0.8169),
    (971,  0.9871);
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        cursor.execute(insert_data_query)
        conn.commit()
        print("Table created and data inserted successfully.")
    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
    finally:
        cursor.close()
        conn.close()

def analyze_data():
    sampling_query = """
    WITH ordered_images AS (
        -- Order images by score descending and ascending, assigning row numbers --
        SELECT image_id, score,
               ROW_NUMBER() OVER (ORDER BY score DESC) AS row_num_desc,
               ROW_NUMBER() OVER (ORDER BY score ASC) AS row_num_asc
        FROM unlabeled_image_predictions
    ),
    positive_samples AS (
        -- Select every 3rd image from the highest scores, starting from the first row --
        SELECT image_id, 1 AS weak_label
        FROM ordered_images
        WHERE row_num_desc % 3 = 1
        ORDER BY row_num_desc
        LIMIT 10000
    ),
    negative_samples AS (
        -- Select every 3rd image from the lowest scores, starting from the first row --
        SELECT image_id, 0 AS weak_label
        FROM ordered_images
        WHERE row_num_asc % 3 = 1
        ORDER BY row_num_asc
        LIMIT 10000
    )
    -- Combine positive and negative samples and order by image_id --    
    SELECT image_id, weak_label
    FROM positive_samples
    UNION ALL
    SELECT image_id, weak_label
    FROM negative_samples
    ORDER BY image_id;
    """

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sampling_query)
        result = cursor.fetchall()

        for row in result:
            print(f"image_id: {row[0]}, weak_label: {row[1]}")

    except sqlite3.Error as err:
        print(f"SQLite error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    load_data()
    analyze_data()

