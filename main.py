from PyPDF2 import PdfFileReader, PdfFileWriter

pdf = PdfFileReader("") # Local Path for pdf goes here....
pdfW = PdfFileWriter()



for sectionCounter in xrange(len(pdf.getOutlines())):

    for chapterCounter in xrange(len(pdf.getOutlines()[sectionCounter])):
        
        if type(pdf.getOutlines()[sectionCounter]) == type([]):
            if chapterCounter < len(pdf.getOutlines()[sectionCounter]) - 1:
                fileName = "Chapter " + str(pdf.getOutlines()[sectionCounter][chapterCounter]['/Title']).strip() + ".pdf"
                firstPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter][chapterCounter]))
                lastPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter][chapterCounter + 1])) - 1
            elif sectionCounter < len(pdf.getOutlines()) - 1:
                try:
                    firstPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter][chapterCounter]))
                    lastPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter + 1][0])) - 1
                except:
                    firstPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter][chapterCounter]))
                    if sectionCounter < len(pdf.getOutlines()) - 1:
                        lastPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter + 1])) - 1
                    elif sectionCounter == len(pdf.getOutlines()) - 1:
                        lastPageNum = pdf.getNumPages() - 1
        else:
            fileName = "Chapter " + str(pdf.getOutlines()[sectionCounter]['/Title']).strip() + ".pdf"
            firstPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter]))
            try:
                lastPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter + 1][0])) - 1
            except:
                if sectionCounter < len(pdf.getOutlines()) - 1:
                    lastPageNum = int(pdf.getDestinationPageNumber(pdf.getOutlines()[sectionCounter + 1])) - 1
                elif sectionCounter == len(pdf.getOutlines()) - 1:
                    lastPageNum = pdf.getNumPages() - 1
            
        for i in xrange(firstPageNum, lastPageNum + 1):
            pdfW.addPage(pdf.getPage(i))
        f = open(fileName, 'wb')
        print fileName
        pdfW.write(f)
        pdfW = None
        pdfW = PdfFileWriter()

        

