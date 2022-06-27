package org.ascension.addg.gcp.ingestion.file_based.ptransforms;

import com.google.common.base.Preconditions;
import com.typesafe.config.Config;
import org.apache.beam.sdk.io.FileIO;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.values.PCollection;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.lang3.StringEscapeUtils;
import org.apache.commons.lang3.StringUtils;
import org.ascension.addg.gcp.ingestion.file_based.FileBasedIngestion;
import org.ascension.addg.gcp.ingestion.Configuration;
import org.ascension.addg.gcp.ingestion.file_based.core.CsvType;
import org.ascension.addg.gcp.ingestion.file_based.core.IngestionRecord;
import org.ascension.addg.gcp.ingestion.file_based.dofns.ReadCSV;
import org.ascension.addg.gcp.ingestion.file_based.dofns.ReadTarWithCSVs;
import org.ascension.addg.gcp.ingestion.file_based.dofns.ReadZipWithCSVs;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;



