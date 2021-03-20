# Using Python Slim-Buster
FROM koala21/kampangbot:buster
#
# Clone repo and prepare working directory
#
RUN git clone -b Kampang https://github.com/tungauicipiyey/kampang-bot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/tungauicipiyey/kampang-bot/Kampang/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
