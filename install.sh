#!/usr/bin/env bash
DIRNAME=$(dirname $(readlink -f $0))
${DIRNAME}/venv/bin/pip install -r requirements.txt
echo "#!/usr/bin/env bash" > $HOME/bin/tweet
echo "${DIRNAME}/venv/bin/python ${DIRNAME}/main.py \"\$@\"" >> $HOME/bin/tweet
chmod +x $HOME/bin/tweet
echo Happy tweeting
