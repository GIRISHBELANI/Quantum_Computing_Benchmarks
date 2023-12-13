FROM ubuntu:20.04

LABEL Name=QED-C\ 
      Version="0.0.1-beta" 

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget curl gcc python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
  
  

SHELL [ "/bin/bash", "--login", "-c" ]

# Create a non-root user
ARG username=quser
ARG uid=1000
ARG gid=100
ARG broot=./qc-app-oriented-benchmarks
ARG platform=cirq

ENV PLATFORM=$platform
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/quser
ENV BROOT $broot
ENV MINICONDA_VERSION 4.8.3
ENV CONDA_DIR $HOME/miniconda3
ENV CROOT ./qc-app-oriented-benchmarks/_containerbuildfiles/$platform

# copy some support files, not some of these aren't currently used but are here as placeholders
COPY ${CROOT}/requirements.txt /tmp/



# minimize additional layers by combining most of the RUN commands
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    quser && \
    chown $UID:$GID /tmp/requirements.txt


# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_$MINICONDA_VERSION-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# Set the PATH variable for subsequent commands
ENV PATH=$CONDA_DIR/bin:/home/${username}/.local/bin:$PATH


RUN conda install --quiet --yes 'notebook=6.1.4' && \
    conda clean --all -f -y

# Install Rust and Cargo
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
    export PATH="$HOME/.cargo/bin:$PATH" && \
    rustup update
 


# Separate pip install command
RUN pip install --no-cache-dir matplotlib cirq
#RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN jupyter notebook --generate-config


# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]



#switch to non-root user (not sure how to reference ARG or ENV here since those trigger an invalid parameter error)
USER quser

# create a project directory inside user home
ENV PROJECT_DIR $HOME
WORKDIR ${PROJECT_DIR}
ADD ${BROOT}/__data ${PROJECT_DIR}/__data
ADD ${BROOT}/_common/${PLATFORM} ${PROJECT_DIR}/_common
ADD ${BROOT}/amplitude-estimation ${PROJECT_DIR}/amplitude-estimation
ADD ${BROOT}/bernstein-vazirani ${PROJECT_DIR}/bernstein-vazirani
ADD ${BROOT}/deutsch-jozsa ${PROJECT_DIR}/deutsch-jozsa
ADD ${BROOT}/grovers ${PROJECT_DIR}/grovers
ADD ${BROOT}/hamiltonian-simulation ${PROJECT_DIR}/hamiltonian-simulation
ADD ${BROOT}/hhl ${PROJECT_DIR}/hhl
ADD ${BROOT}/hidden-shift ${PROJECT_DIR}/hidden-shift
ADD ${BROOT}/monte-carlo ${PROJECT_DIR}/monte-carlo
ADD ${BROOT}/phase-estimation ${PROJECT_DIR}/phase-estimation
ADD ${BROOT}/quantum-fourier-transform ${PROJECT_DIR}/quantum-fourier-transform
ADD ${BROOT}/shors ${PROJECT_DIR}/shors
ADD ${BROOT}/vqe ${PROJECT_DIR}/vqe

COPY ${BROOT}/benchmarks-cirq.ipynb/ ${PROJECT_DIR}/benchmarks-cirq.ipynb
COPY ${BROOT}/_common/metrics.py ${PROJECT_DIR}/_common

EXPOSE 8886
CMD ["jupyter", "notebook", "--port=8886", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

